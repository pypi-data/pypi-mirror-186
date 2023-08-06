# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 18:46:42 2021

@author: amarmore

Single-song autoencoding paradigm.

See [1 - Chapter 5.4] or [2] for more information.

References
----------
[1] Unsupervised Machine Learning Paradigms for the Representation of Music Similarity and Structure, 
PhD Thesis Marmoret Axel 
(not uploaded yet but will be soon!)
(You should check the website hal.archives-ouvertes.fr/ in case this docstring is not updated with the reference.)

[2] Marmoret, A., Cohen, J.E, and Bimbot, F., "Barwise Compression Schemes 
for Audio-Based Music Structure Analysis"", in: 19th Sound and Music Computing Conference, 
SMC 2022, Sound and music Computing network, 2022.
"""

import as_seg.barwise_input as bi
import barmuscomp.ae_utils as ae_utils
from barmuscomp.model.early_stopping import EarlyStopping
import barmuscomp.model.current_plot as current_plot
import barmuscomp.model.errors as err

import numpy as np
import random
import warnings
import torch
import torch.nn as nn
import torch.nn.functional as F

class GenericAutoencoder(nn.Module):
    """
    General autoencoder, acting as a parent class, specifying the functions shared between models.
    
    This autoencoder does not define an encoder or a decoder, they must be specified in children classes.
    """
    def __init__(self, dim_latent_space = 16, beta = 2, latent_nonlinearity = None, seed = None):
        """
        Constructor of the autoencoder.

        Parameters
        ----------
        dim_latent_space : positive int, optional
            Dimension of the latent space. 
            The default is 16.
        beta : float, optional
            The beta value in the beta-divergence, 
            specifying the loss function between the input and the output. 
            The default is 2 (i.e. Euclidean Loss).
            See [1,2] for details on the beta-divergence.
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
            Raised if the specified nonlinear activation function is unknown.
        
        References
        ----------
        [1] Basu, A., Harris, I.R., Hjort, L.N., and Jones, M.C., "Robust and Efficient
        Estimation by Minimising a Density Power Divergence", in: Biometrika 85.3 (1998),
        pp. 549–559, issn: 00063444.
        
        [2] Marmoret, A., Voorwinden, F., Leplat, V., Cohen, J.E., and Bimbot, F.,
        "Nonnegative Tucker Decomposition with Beta-divergence for Music Structure 
        Analysis of audio signals", in: GRETSI (2022).

        """
        super(GenericAutoencoder, self).__init__()
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        
        self.dim_latent_space = dim_latent_space
        self.beta = beta
        self.seed = seed
        
        if latent_nonlinearity is None:
            self.latent_nonlinearity = None
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
        Encoder default value, raising an error.
        It must be implemented in chlidren classes.
        """
        raise NotImplementedError("To be redefined in children classes")
    
    def decoder(self, z):
        """
        Decoder default value, raising an error.
        It must be implemented in chlidren classes.
        """
        raise NotImplementedError("To be redefined in children classes")
    
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
        
        if self.seed is not None:
            self.apply(lambda layer: ae_utils.seeded_weights_init_kaiming(layer, seed=self.seed))
        else:
            self.apply(ae_utils.random_weights_init_kaiming) # Random initialization of the network
            
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
       
# %% Fully-connected
def get_fc_ssae_projection(spectrogram, compression_dimension, bars, 
                           n_epochs = 1000, lr = 1e-3, beta = 2, latent_nonlinearity = None, seed = None, 
                           subdivision_bars = 96, hop_length = 32, sampling_rate = 44100):
    """
    Return the projection of the barwise content with a Fully-Connected AutoEncoder (SSAE).

    Parameters
    ----------
    spectrogram : numpy array
        The spectrogram to analyze, barwise.
    compression_dimension : positive integer
        Dimension of compression (size of the latent space).
    bars : list of tuples
        List of the bars (start, end), in seconds, to cut the spectrogram at bar delimitation.
    n_epochs : int
        Number of epochs to perform.
    lr : float, optional
        Learning rate of the Network. 
        The default is 1e-3.
    beta, latent_nonlinearity, seed:
        See GenericAutoencoder.
    subdivision_bars : integer, optional
        The number of subdivision of the bar to be contained in each slice of the tensor.
        The default is 96.
    hop_length : integer, optional
        The hop_length used for the computation of the spectrogram.
        It is expressed in terms of number of samples, which are defined by the sampling rate.
        The default is 32.
    sampling_rate : float, optional
        Sampling rate used when computing the spectrogram (typically 44100Hz).
        The default is 44100.

    Returns
    -------
    numpy array
        Compressed matrix (latent representations), of size (bars, compression_dimension).
        
    """
    ae_model = FullyConnectedAutoencoder(input_size_x = subdivision_bars, input_size_y = spectrogram.shape[0], dim_latent_space = compression_dimension, beta = beta, latent_nonlinearity = latent_nonlinearity, seed = seed)
    tensor_barwise_BFT = bi.tensorize_barwise_BFT(spectrogram, bars, hop_length/sampling_rate, subdivision_bars)
    data_loader = ae_utils.generate_flatten_dataloader(tensor_barwise_BFT)
    ae_model, losses = ae_model.my_optim_method(n_epochs=n_epochs, data_loader=data_loader, lr=lr, verbose = False, labels = None)
    return ae_model.get_latent_projection(data_loader)

class FullyConnectedAutoencoder(GenericAutoencoder):
    """
    AutoEncoder with fully-connected layers as encoder and decoder.
    """
    def __init__(self, input_size_x, input_size_y, dim_latent_space, beta = 2, latent_nonlinearity = None, seed = None):#, batch_norm = True):
        """
        Constructor of the Fully-connected autoencoder.

        Parameters
        ----------
        input_size_x : integer
            Size of the x axis dimension of the input.
        input_size_y : integer
            Size of the y axis dimension of the input.
        dim_latent_space, beta, latent_nonlinearity, seed:
            See GenericAutoencoder.

        """
        super().__init__(dim_latent_space, beta = beta, latent_nonlinearity = latent_nonlinearity, seed = seed)
        self.fc = nn.Linear(in_features=input_size_x * input_size_y, out_features=128)
        self.fc_2 = nn.Linear(in_features=128, out_features=dim_latent_space)
        self.i_fc = nn.Linear(in_features=dim_latent_space, out_features=128)
        self.i_fc_2 = nn.Linear(in_features=128, out_features=input_size_x * input_size_y)
        
        # self.batch_norm = batch_norm # DEPRECATED: it should always be designed with batch norm layers.
        # if self.batch_norm:
        self.bn_1 = nn.BatchNorm1d(128)
        self.bn_2 = nn.BatchNorm1d(dim_latent_space)
        self.i_bn_1 = nn.BatchNorm1d(128)
       
    def encoder(self, x):    
        """
        Encoder of the Fully-Connected network.
        Two dense layers, each followed by a batch normalization layer.
        The last layer (the 2nd one) may contain a nonnlinear activation function.
        In that case, the activation function replace the batch normalization layer.
        """
        x = F.relu(self.fc(x))
        x = self.bn_1(x)
        x = self.fc_2(x)
        if self.latent_nonlinearity is None:
            return self.bn_2(x)
        else:
            return self.latent_nonlinearity(x)

        
    # def encoder(self, x):
    #     """
    #     Encoder definition.
    #     Switch between an encoder with and without batch normalization layer.
    #     """
    #     if self.batch_norm:
    #         z = self.bn_encoder(x)
    #     else:
    #         z = self.no_bn_encoder(x)

    #     if self.latent_nonlinearity is not None:
    #         z = self.latent_nonlinearity(z)
    #     return z
    
    # def no_bn_encoder(self, x):
    #     """
    #     Encoder without batch normlization layers.
    #     """
    #     x = F.relu(self.fc(x))
    #     return self.fc_2(x)
        

    def decoder(self, z):
        """
        Decoder of the Fully-Connected network.
        Two dense layers. The first one is followed by a batch normalization layer.
        """
        x = F.relu(self.i_fc(z))
        x = self.i_bn_1(x)
        x_hat = self.i_fc_2(x)
        
        # To compute the beta-divergence, needing nonnegative outputs
        x_hat = F.relu(x_hat) # !!! Introduces a hugh bias when the feature is negative ! (Log MEl, MFCC)
        # TODO: Experiences should account for this bias, i.e. be redone.
        return x_hat
    
    # def decoder(self, z):
    #     """
    #     Decoder definition.
    #     Switch between a decoder with and without batch normalization layer.
    #     """
    #     if self.batch_norm:
    #         return self.bn_decoder(z)
    #     else:
    #         return self.no_bn_decoder(z)
        
    
    # def no_bn_decoder(self, z):
    #     """
    #     Decoder without batch normlization layers.
    #     """
    #     x = F.relu(self.i_fc(z))
    #     x_hat = self.i_fc_2(x)
        
    #     # To compute the beta-divergence, needing nonnegative outputs
    #     x_hat = F.relu(x_hat) # !!! Introduces a hugh bias when the feature is negative ! (Log MEl, MFCC)
    #     return x_hat
    
# %% Convolutional
def get_conv_ssae_projection(spectrogram, compression_dimension, bars, 
                             n_epochs = 1000, lr = 1e-3, beta = 2, latent_nonlinearity = None, seed = None, 
                             subdivision_bars = 96, hop_length = 32, sampling_rate = 44100):
    """
    Return the projection of the barwise content with a convolutional AutoEncoder (SSAE).

    Parameters
    ----------
    spectrogram : list of list of floats or numpy array
        The spectrogram to analyze, barwise.
    compression_dimension : positive integer
        Dimension of compression (size of the latent space).
    bars : list of tuples
        List of the bars (start, end), in seconds, to cut the spectrogram at bar delimitation.
    n_epochs : int
        Number of epochs to perform.
    lr : float, optional
        Learning rate of the Network. 
        The default is 1e-3.
    beta, latent_nonlinearity, seed:
        See GenericAutoencoder.
    subdivision_bars : integer, optional
        The number of subdivision of the bar to be contained in each slice of the tensor.
        The default is 96.
    hop_length : integer, optional
        The hop_length used for the computation of the spectrogram.
        It is expressed in terms of number of samples, which are defined by the sampling rate.
        The default is 32.
    sampling_rate : float, optional
        Sampling rate used when computing the spectrogram (typically 44100Hz).
        The default is 44100.

    Returns
    -------
    numpy array
        Compressed matrix (latent representations), of size (bars, compression_dimension).
        
    """
    ae_model = ConvolutionalAutoencoder(input_size_x = subdivision_bars, input_size_y = spectrogram.shape[0], dim_latent_space = compression_dimension, beta = beta, latent_nonlinearity = latent_nonlinearity, seed = seed)
    tensor_barwise_BFT = bi.tensorize_barwise_BFT(spectrogram, bars, hop_length/sampling_rate, subdivision_bars)
    data_loader = ae_utils.generate_dataloader(tensor_barwise_BFT)
    ae_model, losses = ae_model.my_optim_method(n_epochs=n_epochs, data_loader=data_loader, lr=lr, verbose = False, labels = None)
    return ae_model.get_latent_projection(data_loader)

class ConvolutionalAutoencoder(GenericAutoencoder):
    """
    Autoencoder with Convolutional layers as encoder and decoder.
    """
    def __init__(self, input_size_x, input_size_y, dim_latent_space, beta = 2, latent_nonlinearity = None, seed = None):
        """
        Constructor of the Convolutional autoencoder.

        Parameters
        ----------
        input_size_x : integer
            Size of the x axis dimension of the input.
        input_size_y : integer
            Size of the y axis dimension of the input.
        dim_latent_space, beta, latent_nonlinearity, seed:
            See GenericAutoencoder.
            
        """
        super().__init__(dim_latent_space, beta = beta, latent_nonlinearity = latent_nonlinearity, seed = seed)
        self.input_size_pool_y = int(input_size_y/4) # input_size / pool ## NOTE: Doesn't work for odd input sizes (in reconstruction), so TODO.
        self.input_size_pool_x = int(input_size_x/4) # input_size / pool
        
        # Encoder
        ## Convolutional layers
        self.conv1 = nn.Conv2d(1, 4, 3, padding=1)  
        self.conv2 = nn.Conv2d(4,16, 3, padding=1)
        self.pool = nn.MaxPool2d(2, 2)
        self.flatten = nn.Flatten()

        ## Fully-connected controling latent space size.
        in_features = 16 * self.input_size_pool_x * self.input_size_pool_y # nb_kernels_last_conv * (input_size / pool)
        self.fc = nn.Linear(in_features=in_features, out_features=dim_latent_space)
        
        # Decoder
        ## Inverse of previous FC
        self.i_fc = nn.Linear(in_features=dim_latent_space, out_features=in_features)

        # Transposed conv layers
        self.t_conv1 = nn.ConvTranspose2d(16, 4, 3, stride=2, padding=1, output_padding=1)
        self.t_conv2 = nn.ConvTranspose2d(4, 1, 3, stride=2, padding=1, output_padding=1)
        
        self.bn_1 = nn.BatchNorm2d(4)
        self.bn_2 = nn.BatchNorm2d(16)
        self.bn_fc = nn.BatchNorm1d(dim_latent_space)
        
        self.i_bn_fc = nn.BatchNorm1d(16 * self.input_size_pool_y * self.input_size_pool_x)
        self.i_bn_1 = nn.BatchNorm2d(4)
       
           
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
        x = F.relu(self.conv1(x))
        x = self.pool(x)
        x = self.bn_1(x)
        x = F.relu(self.conv2(x))
        x = self.pool(x)
        x = self.bn_2(x)
        
        x = self.flatten(x)
        x = self.fc(x)
        if self.latent_nonlinearity is None:
            return self.bn_fc(x)
        else:
            return self.latent_nonlinearity(x)
        
    def decoder(self, z):
        """
        Decoder of the Convolutioanl autoencoder.
        It is implemented as the inverse of the encoder, with a dense layer
        followed by two transposed convolution layers.
        The two first layers implement a batch normalization layer, but not the last one
        (i.e. no batch normalization before the reconstruction).
        """
        x = self.i_fc(z)
        x = self.i_bn_fc(x)
        x = x.view((x.shape[0], 16, self.input_size_pool_y, self.input_size_pool_x))
        x = F.relu(self.t_conv1(x))
        x = self.i_bn_1(x)
        x_hat = self.t_conv2(x)
        
        # To compute the beta-divergence, needing nonnegative outputs
        x_hat = F.relu(x_hat) # !!! Introduces a hugh bias when the feature is negative ! (Log MEl, MFCC)
        # TODO: Experiences should account for this bias, i.e. make new experiments.
        return x_hat

    
class ConvolutionalAutoencoderTriplet(ConvolutionalAutoencoder):
    """
    Class defining AutoEncoders used to compress barwise representation of a song, with an added Triplet loss to regularize the latent space.
    This triplet loss is designed to favor the bars which are very similar in the initial representation, 
    and to scatter bars which are very dissimilar.
    The positive (similar) and negative (dissimilar) examples are chosen by thresholding the autosimilarity matrix,
    and taking either the most or least similar examples (hence, two thresolds parameters are to be defined, see my_optim_method()).
    
    For more information, refer to [1 - Chapter 5.4.5]
    
    References
    ----------
    [1] Unsupervised Machine Learning Paradigms for the Representation of Music Similarity and Structure, 
    PhD Thesis Marmoret Axel 
    (not uploaded yet but will be soon!)
    (You should check the website hal.archives-ouvertes.fr/ in case this docstring is not updated with the reference.)
    """
    def __init__(self, input_size_x, input_size_y, dim_latent_space, beta = 2, latent_nonlinearity = None, seed = None, triplet_lambda = 1, triplet_type = "simple", triplet_margins = [1]):
        """
        Constructor of the triplet-loss regularized convolutional autoencoder.
        
        input_size_x, input_size_y, dim_latent_space, beta, latent_nonlinearity, seed,
            See parent class (ConvolutionalAutoencoder)
        triplet_lambda : float, optional
            Ponderation for the triplet loss in the mixed loss. The default is 1.
        triplet_type : string, optional
            Type of triplet loss, either simple or double.
             - "simple" refer to the standard triplet loss,
             - "double" refer to the triplet loss with a positive and a negative margin.
             Both triplet losses are introduced in [2], respectively as triplet loss 1 and triplet loss 3.
            The default is "simple".
        triplet_margins : array of ints, optional
            Margins for both triplet losses.
            "simple" triplet loss uses one argument in the array, and "double" uses two, in the order [positive_margin, negative_margin].
            The default is "[1]".
        
        References
        ----------
        [2] Ho, K., Keuper, J., Pfreundt, F. J., & Keuper, M. (2021, January). 
        Learning embeddings for image clustering: An empirical study of triplet loss approaches. 
        In 2020 25th International Conference on Pattern Recognition (ICPR) (pp. 87-94). IEEE.

        """

        super().__init__(input_size_x, input_size_y, dim_latent_space, beta = beta, latent_nonlinearity = latent_nonlinearity, seed = seed)
        self.triplet_lambda = triplet_lambda
        if triplet_type == "simple":
            self.triplet_function = ae_utils.TripletLoss(margin = triplet_margins[0])
        elif triplet_type == "double":
            self.triplet_function = ae_utils.TripletLossDoubleMargin(pos_margin = triplet_margins[0], neg_margin = triplet_margins[1])
        else:
            raise err.InvalidArgumentValueException(f"Triplet loss type not understood: {triplet_type}")

    def forward(self, anchor, positive, negative):
        """
        Forward pass: pass all examples based on the parent class (anchor, positive and negative).
        """
        x_hat_a, z_a = super().forward(anchor)
        x_hat_p, z_p = super().forward(positive)
        x_hat_n, z_n = super().forward(negative)
        return x_hat_a, z_a, x_hat_p, z_p, x_hat_n, z_n
    
    def my_optim_method(self, n_epochs, data_loader, lr=1e-2, verbose = False, labels = None, early_stop_patience = 100, regenerate_data_loader = True, tensor_barwise = None, thresholds_data_loader = [0.1, 0.5]):
        """
        Default optimization method.
        
        This method is to be called in order to optimize the network.

        Parameters
        ----------
        n_epochs, data_loader, lr, verbose, labels, early_stop_patience
            See grand-parent Class (GenericAutoencoder)
        regenerate_data_loader : boolean, optional
            Boolean specifying whether the positive and negative examples needs to be recomputed at each epoch.
            The default is True (i.e. regenrating positive and negative example at each epoch).
            This is made to counter the small numbers of exceprts in our original formulation
            (~100 examples per epoch, each of dimension ~10000, hence largely higher.)
        tensor_barwise : None or numpy.array, optional
            Only used if regenerate_data_loader is set to True.
            Original tensor_barwise, on which is computed the optimization, to regenrate positive and negative examples. 
            The default is None. Should not be set to None if regenerate_data_loader is set to True.
        thresholds_data_loader : list of floats, each 0 \leq float \leq 1, optional
            The thresholds for sampling positive and negative examples, based on the initial similarity between pairs of bars
            (repsectively for positive and negative examples).
            The default is [0.1, 0.5], 
            i.e. positive examples are taken from the 10% most similar bars, and negative from the 50% least similar bars.

        Returns
        -------
        See grand-parent Class (GenericAutoencoder)

        """
        self = self.to(self.device)
        #print(f"Using {self.device}")
        es = EarlyStopping(patience=early_stop_patience)
        
        nb_bars = 0
        for iter_dl, _, _ in data_loader:
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
        
        if self.seed is not None:
            self.apply(lambda layer: ae_utils.seeded_weights_init_kaiming(layer, seed=self.seed))
        else:
            self.apply(ae_utils.random_weights_init_kaiming) # Random initialization of the network

        triplet_loss_function = torch.jit.script(self.triplet_function)

        for epoch in range(1, n_epochs+1):
            total_loss_epoch = 0.0
            if regenerate_data_loader:
                data_loader, _ = ae_utils.generate_triplet_dataloader(tensor_barwise, top_partition = thresholds_data_loader[0], medium_partition = thresholds_data_loader[1])
            for anchor, positive, negative in data_loader:
                anchor = torch.reshape(anchor, (anchor.shape[0],1, anchor.shape[1],anchor.shape[2]))
                anchor = anchor.float().to(self.device)
                positive = torch.reshape(positive, (positive.shape[0],1, positive.shape[1],positive.shape[2]))
                positive = positive.float().to(self.device)
                negative = torch.reshape(negative, (negative.shape[0],1, negative.shape[1],negative.shape[2]))
                negative = negative.float().to(self.device)
                
                optimizer.zero_grad()
                
                x_hat_a, z_a, x_hat_p, z_p, x_hat_n, z_n = self.forward(anchor, positive, negative) # Forward
        
                # Recon losses
                recons_loss_a = recons_loss(x_hat_a, anchor)
                recons_loss_p = recons_loss(x_hat_p, positive)
                recons_loss_n = recons_loss(x_hat_n, negative)
                # Triplet loss
                triplet_loss_val = triplet_loss_function(z_a, z_p, z_n)
                # Mixed loss
                loss = recons_loss_a + recons_loss_p + recons_loss_n + self.triplet_lambda * triplet_loss_val
                loss.backward() # Backward
                optimizer.step()
                total_loss_epoch += loss.item() * anchor.size(0)
            total_loss_epoch = total_loss_epoch/nb_bars
            losses.append(total_loss_epoch)
            scheduler.step(total_loss_epoch)
            
            if verbose:
                total_loss_epoch = total_loss_epoch
                print('Epoch: {} \tCumulated reconstruction loss: {:.6f}'.format(epoch,total_loss_epoch))
                
                if epoch%50 == 0:
                    projection = self.get_latent_projection(data_loader)
                    current_plot.plot_latent_space(projection, labels = labels)
                    
            if es.step(total_loss_epoch):
                if verbose:
                    print(f"Early stopping criterion has been met in {epoch}, computation is stopped.")
                break 
        return self, losses
    
    def get_latent_projection(self, data_loader):
        """
        Returns the latent representation on a given network, redefined for handling the triplets.
        
        Used after optimization to access to the latent representations.
        """
        all_data = []
        for spec, _, _ in data_loader:
            spec = spec.float().to(self.device)
            spec = torch.reshape(spec, (spec.shape[0], 1, spec.shape[1], spec.shape[2]))
            spec_recons, z = super().forward(spec)
            for elt in z:
                all_data.append(elt.cpu().detach().numpy())
        return all_data


####################################### Sparse networks, deprecated !!!
class ConvolutionalAutoencoderSparse(ConvolutionalAutoencoder):
    """
    Class defining the Sparse Convolutional Neural Network (SAE) used to compress barwise representation of a song.
    
    This SAE is the same CNN than the previously defined (``ConvolutionalAutoencoder'') but adds a saprsity constraint on the latent representation.
    The goal of this sparsity is to disentangle the different dimensions of the latent space.
    """
    def __init__(self, input_size_x, input_size_y, dim_latent_space, sparsity_lambda, norm_tensor, beta = 2):
        """
        Constructor of the network.

        Parameters
        ----------
        input_size_x : int
            The x-axis size of the input matrix.
        input_size_y : int
            The y-axis size of the input matrix.
        dim_latent_space : int, optional
            Dimension of the latent space. The default is 16.
        sparsity_lambda : float
            Ponderation parameter for the sparsity constraint (on z).
        norm_tensor : float
            Norm of the tensor on which to optimize, used as a normalization for the sparsity parameter.

        Raises
        ------
        err.OutdatedBehaviorException.
            Raised if ``nonnegative'' argument is set to True.

        Returns
        -------
        None.

        """
        if nonnegative:
            raise err.OutdatedBehaviorException("So-called ``nonnegative networks'' are not supported anymore, as they weren't succesful.") from None
        
        super().__init__(input_size_x, input_size_y, dim_latent_space, beta = beta)
        self.sparsity_lambda_normed = sparsity_lambda #round(sparsity_lambda/norm_tensor, 8) ## Normalized sparsity parameter

    def my_optim_method(self, n_epochs, data_loader, lr=1e-2, verbose = False, labels = None, early_stop_patience = 100):
        """
        Optimization method. Defined directly in the class, in order to be called from the object.

        Parameters
        ----------
        n_epochs : int
            Number of epochs to perform.
        data_loader : torch.DataLoader
            The DataLoader to optimize on.
        lr : float, optional
            Learning rate of the Network. The default is 1e-3.
        early_stop_patience : int, optional
            Patience for the number of consecutive epochs.
            If the loss doesn't improve during early_stop_patience epochs, the optimization stops. The default is 100.
        verbose : boolean, optional
            Argument to print the evolution of the optimization.
            Prints the current loss and plot a view of the autosimilarity of latent variables and a PCA of the latent space.
            The default is False.
        labels : None or array, optional
            Only used if verbose is set to True.
            If labels are set, they will be used to color the output of PCA projection.
            If they are set to None, no label is used. The default is None.

        Returns
        -------
        ConvolutionalAutoencoderSparse
            Returns the Network.
            Note: not mandatory (as the object needs to be instanciated to call this method), but returned as a good practice.

        """
        es = EarlyStopping(patience=early_stop_patience)
        
        recons_loss = nn.MSELoss() # Mean Squared Euclidian loss
        optimizer = torch.optim.Adam(self.parameters(), lr=lr)
        
        # Scheduler to decrease the learning rate when optimization reaches a plateau (20 iterations)
        scheduler = torch.optim.lr_scheduler.ReduceLROnPlateau(optimizer, patience=20, verbose=verbose,min_lr=1e-5) 
        self.apply(ae_utils.seeded_weights_init_kaiming) # Seeded initialization of the network

        for epoch in range(1, n_epochs+1):
            total_loss_epoch = 0.0
            for spec in data_loader:
                spec = spec.float()
        
                optimizer.zero_grad()
                x_hat, z = self.forward(spec) # Forward
                recons_loss_spec = recons_loss(x_hat, spec) # Reconstruction loss
                l1_regularization = torch.abs(z).mean() # L1 reg
                loss = recons_loss_spec + self.sparsity_lambda_normed * l1_regularization # Mixed loss
                loss.backward() # Backward
                optimizer.step()
                total_loss_epoch += loss.item()
            scheduler.step(total_loss_epoch)
            
            if verbose:
                total_loss_epoch = total_loss_epoch
                print('Epoch: {} \tCumulated reconstruction loss: {:.6f}'.format(epoch, total_loss_epoch))
                if epoch%50 == 0:
                    projection = self.get_latent_projection(data_loader)
                    current_plot.plot_latent_space(projection, labels = labels)
                    
            if es.step(total_loss_epoch):
                if verbose:
                    print(f"Early stopping criterion has been met in {epoch}, computation is stopped.")
                break 
        return self    
