# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 18:46:42 2021

@author: amarmore

Mixing the Nonnegative Tucker Decomposition (NTD) with Autoencoders (Single-Song AutoEncoders).

In short, the idea is to implement an NTD structure in the decoder. See [1 - Chapter 6] for details.

References
----------
[1] Unsupervised Machine Learning Paradigms for the Representation of Music Similarity and Structure, 
PhD Thesis Marmoret Axel 
(not uploaded yet but will be soon!)
(You should check the website hal.archives-ouvertes.fr/ in case this docstring is not updated with the reference.)
"""

import barmuscomp.ae_utils as ae_utils
from barmuscomp.model.early_stopping import EarlyStopping
import barmuscomp.model.current_plot as current_plot
import barmuscomp.model.errors as err

import numpy as np
import random
import warnings
import tensorly as tl
import torch
import torch.nn as nn
import torch.nn.functional as F

class GenericAutoencoderNTD(nn.Module):
    """
    Generic Autoencoder, with NTD decoder.
    
    Hence, the decoder is structured with matrices W, H and the core tensor G.
    """
    def __init__(self,  input_size_x, input_size_y, ntd_dimensions, unfolded_G, W, H, bn_latent_init_stds = None, bn_latent_init_avgs = None, beta = 2, latent_nonlinearity = None, seed = None):
        """
        Constructor of the AE-NTD.

        Parameters
        ----------
        input_size_x : positive int
            Dimension of the x axis (time at barscale). 
        input_size_y : positive int
            Dimension of the y axis (frequency scale). .
        ntd_dimensions : list of integers.
            Dimensions of the factors for NTD 
            (i.e. number of columns of each matrix factor, 
             or , equivalently, dimensions of the core tensor).
        unfolded_G : numpy array
            Initialization for the core tensor G.
            The tensor must be unfolded on the barwise mode.
        W : numpy array
            Initialization for the factor matrix W (frequency mode).
        H : numpy array
            Initialization for the factor matrix H (rhythmic factors).
        bn_latent_init_stds : list of float, optional
            Initialization of the batch normalization layer on the latent space,
            here, the standard deviation.
            If set, they must be computed as the std of the dimensions of the Q matrix.
            The default is None.
        bn_latent_init_avgs :list of float, optional
            Initialization of the batch normalization layer on the latent space,
            here, the averages.
            If set, they must be computed as the averages of the dimensions of the Q matrix.
            The default is None.
        beta : float, optional
            The beta value in the beta-divergence, 
            specifying the loss function between the input and the output. 
            The default is 2 (i.e. Euclidean Loss).
        latent_nonlinearity : string, optional
            A value specfiying the choice for a nonlinear activation function
            constraining the values of the latent representation.
            The default is None, meaning no nonlinear activation function.
        seed : float, optional
            A seed to fix pseudo-randomness.
            The default is None, meaning no seed.

        Raises
        ------
        InvalidArgumentValueException
            Raised if arguments are not accurately set.

        """
        if W is None and input_size_y == None:
            raise err.InvalidArgumentValueException("You must specify either W or its size. Here, both args 'W' and 'input_size_y' are set to None.")
        if H is None and input_size_x == None:
            raise err.InvalidArgumentValueException("You must specify either H or its size. Here, both args 'H' and 'input_size_x' are set to None.")
        super(GenericAutoencoderNTD, self).__init__()
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        
        self.input_size_x = input_size_x
        self.input_size_y = input_size_y
        
        self.beta = beta
        self.ntd_dimensions = ntd_dimensions
        
        if seed is not None:
            torch.manual_seed(seed)
        
        if W is None:
            self.W_torch = nn.Parameter(torch.empty(input_size_y, ntd_dimensions[0]), requires_grad = True)
            nn.init.kaiming_uniform_(self.W_torch, mode='fan_out', nonlinearity='relu')
        else:
            self.W_torch = nn.Parameter(torch.tensor(W).float().contiguous(), requires_grad = True)

        if H is None:
            self.H_torch = nn.Parameter(torch.empty(input_size_x, ntd_dimensions[1]), requires_grad = True)
            nn.init.kaiming_uniform_(self.H_torch, mode='fan_out', nonlinearity='relu')
        else:
            self.H_torch = nn.Parameter(torch.tensor(H).float().contiguous(), requires_grad = True)

        if unfolded_G is None:
            self.unfolded_G_torch = nn.Parameter(torch.empty(ntd_dimensions[2], ntd_dimensions[0]*ntd_dimensions[1]), requires_grad = True)        
            nn.init.kaiming_uniform_(self.unfolded_G_torch, mode='fan_out', nonlinearity='relu')
        else:
            self.unfolded_G_torch = nn.Parameter(torch.tensor(unfolded_G).float().contiguous(), requires_grad = True)
            
        if latent_nonlinearity is None:
            self.latent_nonlinearity = None

            self.bn_latent = nn.BatchNorm1d(ntd_dimensions[2])
            if bn_latent_init_stds != None:
                self.bn_latent.weight.data = torch.tensor(bn_latent_init_stds).float() if not torch.is_tensor(bn_latent_init_stds) else bn_latent_init_stds.clone().detach()
            if bn_latent_init_avgs != None:
                self.bn_latent.bias.data = torch.tensor(bn_latent_init_avgs).float() if not torch.is_tensor(bn_latent_init_avgs) else bn_latent_init_avgs.clone().detach()

        elif latent_nonlinearity == "sigmoid":
            self.latent_nonlinearity = nn.Sigmoid()
        # elif latent_nonlinearity == "hardshrink":
        #     self.latent_nonlinearity = nn.Hardshrink(lambd = 0.5)
        elif latent_nonlinearity == "softmax":
            self.latent_nonlinearity = nn.Softmax(dim=1)
        elif latent_nonlinearity == "tanh":
            self.latent_nonlinearity = nn.Tanh()
        else:
            raise err.InvalidArgumentValueException(f"Activation function not understood for the latent space: {latent_nonlinearity}") from None

    def forward(self, x):
        """
        Forward pass.
        x_hat is the reconstructed input, z is the latent projection.
        """        
        # Encoding
        z = self.encoder(x)
            
        # Decoding
        x_hat = self.decoder(z)

        return x_hat, z
    
    def encoder(self, x):
        """
        Generic encoder, not defined in the parent class, must be redefined in children classes.
        """
        raise NotImplementedError("To be redefined in children classes")
    
    def decoder(self, z):
        """
        NTD based decoder.
        
        It consists of two fully-connected layers, with two relu functions:
            - The first with the structure of the core tensor G,
            - The second with the structure of the Kronecker product between W and H.
        Hence, the decoder fully mimics an NTD, and these matrices may be initialized from the results of an NTD.
        """
        x = F.relu(torch.matmul(z, self.unfolded_G_torch))
        
        w_kron_h = torch.kron(self.W_torch.T, self.H_torch.T)
        mat_mul = torch.matmul(x, w_kron_h)
        x_hat = F.relu(mat_mul)
        
        return x_hat
    
    def my_optim_method(self, n_epochs, data_loader, lr = 1e-3, early_stop_patience = 100, verbose = False, labels = None):
        """
        Default optimization method.
        
        This method is to be called in order to optimize the network.

        Parameters
        ----------
        n_epochs : int
            Number of epochs to perform.
        data_loader : torch.DataLoader
            The DataLoader to optimize on.
        lr : float, optional
            Learning rate of the Network. 
            The default is 1e-3.
        early_stop_patience : int, optional
            Patience for the number of consecutive epochs.
            If the loss doesn't decrease during early_stop_patience epochs, the optimization stops. 
            The default is 100.
        verbose : boolean, optional
            Argument to print the evolution of the optimization.
            Prints the current loss and plots a view of the autosimilarity of 
            latent variables and a PCA of the latent space.
            The default is False.
        labels : None or array, optional
            Only used if verbose is set to True.
            If labels are set, they will be used to color the output of PCA projection.
            If they are set to None, no label is used. The default is None.

        Returns
        -------
        GenericAutoencoder
            The instance of the network, optimized.
            NB: it is not required to return the network, this is rather implemented 
            in order to avoid some "unintenional" optimization 
            (as it forces a human user to notice that something is returned,
             and hence that some code was run).
        losses : list of positive floats
            The loss values at each iteration.

        """
        self = self.to(self.device)
        #print(f"Using {self.device}")
        es = EarlyStopping(patience=early_stop_patience)
        
        nb_bars = 0
        for iter_dl in data_loader:
            nb_bars += iter_dl.shape[0]

        if self.beta == 2:
            recons_loss = nn.MSELoss() # Mean Squared Euclidian loss
        else:
            recons_loss = ae_utils.BetaDivergenceLoss(beta = self.beta)
            # recons_loss = torch.jit.script(ae_utils.BetaDivergenceLoss(beta = self.beta))
        losses = []
            
        optimizer = torch.optim.Adam(self.parameters(), lr=lr)
        
        # Scheduler to decrease the learning rate when optimization reaches a plateau (20 iterations)
        scheduler = torch.optim.lr_scheduler.ReduceLROnPlateau(optimizer, patience=20, verbose=verbose,min_lr=1e-5)
            
        for epoch in range(1, n_epochs+1):
            total_loss_epoch = 0.0
            for spec in data_loader:
                spec = spec.float().to(self.device)
                optimizer.zero_grad()
                spec_recons, z = self.forward(spec) # Forward pass
                loss = recons_loss(spec_recons, spec) # Loss
                loss.backward() # Backward pass
                optimizer.step() # Optimizes the net with grads
                
                total_loss_epoch += loss.item() * spec.size(0)
            total_loss_epoch = total_loss_epoch/nb_bars
            losses.append(total_loss_epoch)
            scheduler.step(total_loss_epoch) # scheduler for the decrease of lr on a plateau
                
            if verbose:
                print('Epoch: {} \tCumulated reconstruction loss: {:.6f}'.format(epoch, total_loss_epoch))
                if epoch%50 == 0:
                    projection = self.get_latent_projection(data_loader)
                    current_plot.plot_latent_space(projection, labels = labels)
                    
            if es.step(total_loss_epoch): # Checks if loss has decreased, to stop the optimization if performances don't increase for early_stop_patience epochs.
                if verbose:
                    print(f"Early stopping criterion has been met in {epoch}, computation is stopped.")
                break 
        return self, losses
    
    def get_latent_projection(self, data_loader):
        """
        Returns the latent representation on a given network.
        
        Used after optimization to access to the latent representations.
        
        Parameters
        ----------
        data_loader : torch.DataLoader
            The DataLoader to project (intended to be the same that the one used for optimization).

        Returns
        -------
        all_data : numpy array
            The latent representation for each data in the dataset.

        """
        all_data = []
        for spec in data_loader:
            spec = spec.float().to(self.device)
            spec_recons, z = self.forward(spec)
            for elt in z:
                all_data.append(elt.cpu().detach().numpy())
        return all_data
    
    def get_W(self):
        """
        Method returning the nonnegative part of W, used for reconstructing patterns and studying the decoder.
        """
        return F.relu(self.W_torch).cpu().detach().numpy()
    
    def get_H(self):
        """
        Method returning the nonnegative part of H, used for reconstructing patterns and studying the decoder.
        """
        return F.relu(self.H_torch).cpu().detach().numpy()
    
    def get_G(self):
        """
        Method returning the nonnegative part of the G core tensor (refolded into a tensor), used for reconstructing patterns and studying the decoder.
        """
        return tl.fold(F.relu(self.unfolded_G_torch).cpu().detach().numpy(), mode = 2, shape = (self.ntd_dimensions[0], self.ntd_dimensions[1], self.ntd_dimensions[2]))
    
    def get_pattern_list(self):
        """
        Method computing all patterns and returning them.
        """
        nn_g = F.relu(self.unfolded_G_torch)
        kron_T = torch.kron(self.W_torch.T, self.H_torch.T)
        pat_torch = F.relu(torch.matmul(nn_g, kron_T)).cpu().detach().numpy()
        return np.reshape(pat_torch,(self.ntd_dimensions[2], self.input_size_y, self.input_size_x))
       
# %% Fully-connected
class FullyConnectedAutoencoderNTD(GenericAutoencoderNTD):
    """
    AE-NTD with a fully-connected (2 layers) encoder.
    """
    def __init__(self, input_size_x, input_size_y, ntd_dimensions, unfolded_G, W, H, bn_latent_init_stds = None, bn_latent_init_avgs = None, beta = 2, latent_nonlinearity = None, seed = None):
        """
        Constructor.
        
        See parent class for parameters.
        """
        super().__init__(input_size_x = input_size_x, input_size_y = input_size_y, ntd_dimensions = ntd_dimensions, unfolded_G = unfolded_G, W = W, H = H, bn_latent_init_stds = bn_latent_init_stds, bn_latent_init_avgs = bn_latent_init_avgs, 
                         beta = beta, latent_nonlinearity = latent_nonlinearity, seed = seed)

        # Encoder
        self.enc1 = nn.Linear(in_features=input_size_x * input_size_y, out_features=ntd_dimensions[0]*ntd_dimensions[1])
        self.enc2 = nn.Linear(in_features=ntd_dimensions[0]*ntd_dimensions[1], out_features=ntd_dimensions[2])

        self.bn1 = nn.BatchNorm1d(ntd_dimensions[0]*ntd_dimensions[1])

        # if seed is not None: # Should aready be set in parent class
        #     torch.manual_seed(seed)

        nn.init.kaiming_uniform_(self.enc1.weight, mode='fan_out', nonlinearity='relu')
        nn.init.zeros_(self.enc1.bias)
        # nn.init.kaiming_uniform_(self.enc2.weight, a=-1e-5, mode='fan_out', nonlinearity='leaky_relu')
        nn.init.kaiming_uniform_(self.enc2.weight, mode='fan_out', nonlinearity='relu')
        nn.init.zeros_(self.enc2.bias)

    def encoder(self, x):
        """
        Encoder of the Fully-Connected network.
        Two dense layers, each followed by a batch normalization layer.
        The last layer (the 2nd one) may contain a nonnlinear activation function.
        In that case, the activation function replace the batch normalization layer.
        """
        x = F.relu(self.enc1(x))
        x = self.bn1(x)

        x = self.enc2(x)
        
        if self.latent_nonlinearity is not None:
            z = self.latent_nonlinearity(x)
        else:
            x = self.bn_latent(x)
            #z = F.leaky_relu(x, negative_slope = -1e-5)
            z = torch.add(F.relu(x), 1e-10)

        return z
    
# %% Convolutional
class ConvolutionalAutoencoderNTD(GenericAutoencoderNTD):
    """
    AE-NTD with a convolutional (3 layers) encoder.
    """
    def __init__(self, input_size_x, input_size_y, ntd_dimensions, unfolded_G, W, H, bn_latent_init_stds = None, bn_latent_init_avgs = None, beta = 2, latent_nonlinearity = None, seed = None):
        """
        Constructor.
        
        See parent class for parameters.
        """
        super().__init__(input_size_x = input_size_x, input_size_y = input_size_y, ntd_dimensions = ntd_dimensions, unfolded_G = unfolded_G, W = W, H = H, bn_latent_init_stds = bn_latent_init_stds, bn_latent_init_avgs = bn_latent_init_avgs, 
                         beta = beta, latent_nonlinearity = latent_nonlinearity, seed = seed)
        
        self.input_size_pool_y = int(input_size_y/4) # input_size / pool ## NOTE: Doesn't work for odd input sizes (in reconstruction), so TODO.
        self.input_size_pool_x = int(input_size_x/4) # input_size / pool
        
        self.input_size_x = input_size_x
        self.input_size_y = input_size_y
        
        # if seed is not None: # Should aready be set in parent class
        #     torch.manual_seed(seed)
        
        # Encoder
        ## Convolutional layers
        self.conv1 = nn.Conv2d(1, 4, 3, padding=1)  
        self.conv2 = nn.Conv2d(4,16, 3, padding=1)
        nn.init.kaiming_uniform_(self.conv1.weight, mode='fan_out', nonlinearity='relu')
        nn.init.zeros_(self.conv1.bias)
        nn.init.kaiming_uniform_(self.conv2.weight, mode='fan_out', nonlinearity='relu')
        nn.init.zeros_(self.conv2.bias)
        
        self.bn_1 = nn.BatchNorm2d(4)
        self.bn_2 = nn.BatchNorm2d(16)
        
        self.pool = nn.MaxPool2d(2, 2)
        self.flatten = nn.Flatten()

        ## Fully-connected controling latent space size.
        in_features = 16 * self.input_size_pool_x * self.input_size_pool_y # nb_kernels_last_conv * (input_size / pool)
        self.fc = nn.Linear(in_features=in_features, out_features=ntd_dimensions[2])
        
        # nn.init.kaiming_uniform_(self.fc.weight, a=-1e-5, mode='fan_out', nonlinearity='leaky_relu')
        nn.init.kaiming_uniform_(self.fc.weight, mode='fan_out', nonlinearity='relu')
        nn.init.zeros_(self.fc.bias)
        
    def encoder(self, x):
        """
        Encoder of the Covolutional Autoencoder.
        It is implemented with two convolutional layers, 
        each followed by a ReLU, a pooling layer, and a batch normalization layer.
        After these convolutional blocks, a fully-connected layer is implemented,
        leading to the latent representations.
        A batch normalization layer is implemented after the dense layer,
        but it can be replaced by a nonlinear activation function if specified.
        """
        self.batch_size = x.shape[0]
        
        x = F.relu(self.conv1(x))
        x = self.pool(x)
        x = self.bn_1(x)
        x = F.relu(self.conv2(x))
        x = self.pool(x)
        x = self.bn_2(x)
        
        x = self.flatten(x)
        x = self.fc(x)
        
        if self.latent_nonlinearity is not None:
            z = self.latent_nonlinearity(x)
        else:
            x = self.bn_latent(x)
            z = torch.add(F.relu(x), 1e-10)
        return z
    
    def forward(self, x):
        """
        Redefinition of the forward method, in order to account for the matrix shape of the input (conv network).
        """
        batch_size = x.shape[0]
        x_hat, z = super().forward(x)
        x_hat = x_hat.reshape((batch_size, 1, self.input_size_y, self.input_size_x))
        return x_hat, z
