# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 18:34:29 2021

@author: amarmore

Useful functions for handling single-song compression paradigms.
"""

import as_seg.data_manipulation as dm
import as_seg.autosimilarity_computation as as_comp
import barmuscomp.model.errors as err

import copy
import random
import numpy as np
import tensorly as tl
import torch
import torch.nn as nn
import matplotlib.pyplot as plt
import matplotlib.cm as cm

# %% Dataloaders generation
def generate_dataloader(tensor_barwise, batch_size = None):
    """
    Generates a torch.DataLoader from the tensor spectrogram.
    
    Each barwise spectrogram is a matrix (frequency, time at barscale).

    Parameters
    ----------
    tensor_barwise : np.array tensor
        The tensor-spectrogram as a np.array.

    Returns
    -------
    data_loader : torch.DataLoader
        torch.DataLoader for this song and this tensor-spectrogram.
    """
    if batch_size == None:
        batch_size = tensor_barwise.shape[0]
    num_workers = 0
    nb_bars = tensor_barwise.shape[0]
    freq_len, subdivision_bars = tensor_barwise.shape[1], tensor_barwise.shape[2]

    barwise_spec = copy.deepcopy(tensor_barwise)
    
    barwise_spec = barwise_spec.reshape((nb_bars, 1, freq_len, subdivision_bars))
    data_loader = torch.utils.data.DataLoader(barwise_spec, batch_size=batch_size, num_workers=num_workers)
    
    return data_loader
    
def generate_flatten_dataloader(tensor_barwise, batch_size = None):
    """
    Generates a torch.DataLoader from the tensor spectrogram.
    
    Each barwise spectrogram is a vector (frequency x time at barscale).

    Parameters
    ----------
    tensor_barwise : np.array tensor
        The tensor-spectrogram as a np.array.

    Returns
    -------
    data_loader : torch.DataLoader
        torch.DataLoader for this song and this tensor-spectrogram.
    """
    if batch_size == None:
        batch_size = tensor_barwise.shape[0]
    num_workers = 0
    nb_bars = tensor_barwise.shape[0]
    freq_len, subdivision_bars = tensor_barwise.shape[1], tensor_barwise.shape[2]

    barwise_spec = copy.deepcopy(tensor_barwise)
    
    flatten_barwise_spec = barwise_spec.reshape((nb_bars, freq_len*subdivision_bars), order="C")
    flatten_simplet_data_loader = torch.utils.data.DataLoader(flatten_barwise_spec, batch_size=batch_size, num_workers=num_workers)
    
    return flatten_simplet_data_loader
    
# %% Deterministic initializations for networks
def seeded_weights_init_kaiming(m, seed = 42): 
    """ 
    Determinstic initialization of weights with Kaiming uniform distribution.

    Parameters
    ----------
    m : torch.nn
        A layer of the network.
    seed : float, optional
        The seed to fix the pseudo-randomness. The default is 42.

    """
    torch.manual_seed(seed)
    #torch.use_deterministic_algorithms(True)
    # if isinstance(m, nn.BatchNorm1d):
    #     nn.init.zeros_(m.bias)
    #     nn.init.ones_(m.weight)
    if isinstance(m, nn.Linear) or isinstance(m, nn.Conv1d) or isinstance(m, nn.ConvTranspose1d) or isinstance(m, nn.Conv2d) or isinstance(m, nn.ConvTranspose2d):
        #nn.init.kaiming_uniform_(m.weight, mode='fan_in', nonlinearity='relu')
        nn.init.kaiming_uniform_(m.weight, mode='fan_out', nonlinearity='relu')
        if m.bias is not None:
            nn.init.zeros_(m.bias)
     
def random_weights_init_kaiming(m): 
    """
    Random initialization of weights with Kaiming uniform distribution.

    Parameters
    ----------
    m : torch.nn
        A layer of the network.
    """
    #torch.use_deterministic_algorithms(False)
    if isinstance(m, nn.Linear) or isinstance(m, nn.Conv1d) or isinstance(m, nn.ConvTranspose1d) or isinstance(m, nn.Conv2d) or isinstance(m, nn.ConvTranspose2d):
        #nn.init.kaiming_uniform_(m.weight, mode='fan_in', nonlinearity='relu')
        nn.init.kaiming_uniform_(m.weight, mode='fan_out', nonlinearity='relu')
        if m.bias is not None:
            nn.init.zeros_(m.bias)

def seeded_weights_init_xavier(m):
    """
    Determinstic initialization of weights with Xavier uniform distribution.

    Parameters
    ----------
    m : torch.nn
        A layer of the network.
    """    
    torch.manual_seed(42)
    torch.use_deterministic_algorithms(True)
    # if isinstance(m, nn.BatchNorm1d):
    #     nn.init.zeros_(m.bias)
    #     nn.init.ones_(m.weight)
    if isinstance(m, nn.Linear) or isinstance(m, nn.Conv1d) or isinstance(m, nn.ConvTranspose1d) or isinstance(m, nn.Conv2d) or isinstance(m, nn.ConvTranspose2d):
        nn.init.xavier_uniform_(m.weight)
        if m.bias is not None:
            nn.init.zeros_(m.bias)
        
def weights_init_sparse(m):
    """
    Determinstic initialization of weights with sparse initialization.

    Parameters
    ----------
    m : torch.nn
        A layer of the network.
    """   
    if isinstance(m, nn.Conv1d) or isinstance(m, nn.Linear) or isinstance(m, nn.ConvTranspose1d):
        torch.nn.init.sparse_(m.weight, sparsity = 0.1)
        
def weights_ones(m):
    """
    Determinstic initialization of weights with layers full of ones.

    Parameters
    ----------
    m : torch.nn
        A layer of the network.
    """   
    if isinstance(m, nn.Linear):# or isinstance(m, nn.ConvTranspose2d):
        nn.init.ones_(m.weight) 
        
# %% Triplet losees
class TripletLoss(nn.Module):
    """
    Triplet Loss class, following the Triplet Loss paradigm. See [1] for details.
        
    Comes from: https://www.kaggle.com/hirotaka0122/triplet-loss-with-pytorch
    
    References
    ----------
    [1] Ho, K., Keuper, J., Pfreundt, F. J., & Keuper, M. (2021, January). 
    Learning embeddings for image clustering: An empirical study of triplet loss approaches. 
    In 2020 25th International Conference on Pattern Recognition (ICPR) (pp. 87-94). IEEE.
    """
    
    def __init__(self, margin=1.0):
        """
        Constructor of the loss.

        Parameters
        ----------
        margin : float, optional
            Margin for the triplet loss. The default is 1.0.

        """
        super(TripletLoss, self).__init__()
        self.margin = margin
        
    def calc_euclidean(self, x1, x2):
        """
        Euclidean distance between x1 and x2.
        """
        return (x1 - x2).pow(2).sum(1)
    
    def forward(self, anchor, positive, negative):
        """
        Computes the triplet loss, based on the euclidean distances between samples.
        """
        distance_positive = self.calc_euclidean(anchor, positive)
        distance_negative = self.calc_euclidean(anchor, negative)
        losses = torch.relu(distance_positive - distance_negative + self.margin)
        return losses.mean()
    
class TripletLossDoubleMargin(nn.Module):
    """
    Triplet Loss with positive and negative margins, following the work of [1]
    
    References
    ----------
    [1] Ho, K., Keuper, J., Pfreundt, F. J., & Keuper, M. (2021, January). 
    Learning embeddings for image clustering: An empirical study of triplet loss approaches. 
    In 2020 25th International Conference on Pattern Recognition (ICPR) (pp. 87-94). IEEE.
    """
    def __init__(self, pos_margin=1.0, neg_margin = 3.0):
        """
        Constructor of the loss.

        Parameters
        ----------
        pos_margin : float, optional
            Margin for positive examples. The default is 1.0.
        neg_margin : float, optional
            Margin for negative examples. The default is 3.0.

        """
        super(TripletLossDoubleMargin, self).__init__()
        self.pos_margin = pos_margin
        self.neg_margin = neg_margin
        
    def calc_euclidean(self, x1, x2):
        """
        Euclidean distance between x1 and x2.
        """
        return (x1 - x2).pow(2).sum(1)
    
    def forward(self, anchor, positive, negative):
        """
        Computes the triplet loss, based on the euclidean distances between samples.
        """
        distance_positive = self.calc_euclidean(anchor, positive)
        distance_negative = self.calc_euclidean(anchor, negative)
        losses = torch.relu(self.neg_margin - distance_negative) + torch.relu(distance_positive - self.pos_margin)
        return losses.mean()
    
def generate_triplet_dataloader(tensor_barwise, top_partition = 0.1, medium_partition = 0.5, batch_size = None):
    """
    Generates torch.DataLoaders for TripletLoss, with a positive and a negative example for each bar.
    Positive and negative examples are randomly selected from most similar and less similar bars.
    The similarity is the feature_wise similarity.
    Both arguments ``top_partition'' and ``medium_partition'' are dedicated to thresholding most and less similar for random selection.

    Parameters
    ----------
    tensor_barwise : np.array tensor
        The tensor-spectrogram as a np.array.
    top_partition : float \in [0,1], optional
        Percentage of most similar bars (in feature-wise similarity) on which select a positive example.
        The default is 0.1, corresponding to 10% most similar bars.
    medium_partition : float \in [0,1], optional
        Percentage of less similar bars (in feature-wise similarity) on which select a positive example.
        The default is 0.5, selecting from the 50% least similar bars.

    Returns
    -------
    triplet_data_loader : torch.DataLoader
        torch.DataLoader for this song and this tensor-spectrogram.
        Each barwise spectrogram is kept as a matrix, for convolutional networks.
    flatten_triplet_data_loader : torch.DataLoader
        torch.DataLoader for this song and this tensor-spectrogram.
        On this DataLoader, each barwise spectrogram is flattened, for networks which needs vectors as inputs.

    """
    if batch_size == None:
        batch_size = tensor_barwise.shape[0]
    num_workers = 0
    signal_autosimilarity = as_comp.get_cosine_autosimilarity(tl.unfold(tensor_barwise,0))
    nb_bars = tensor_barwise.shape[0]
    vectorized_spec_dim = tensor_barwise.shape[1]*tensor_barwise.shape[2]
    
    barwise_spec = copy.deepcopy(tensor_barwise)
    triplet_data = []
    flatten_triplet_data = []
    
    # threshed_mat = np.ones((nb_bars, nb_bars))

    high_thresh = int(top_partition * nb_bars) + 1
    medium_thresh = int(medium_partition * nb_bars)

    for index, bar in enumerate(barwise_spec):
        this_bar_similarities = signal_autosimilarity[index]
        highest_indexes = np.argpartition(this_bar_similarities, -high_thresh)[-high_thresh:]
        # threshed_mat[index,highest_indexes] = 2
        # threshed_mat[highest_indexes,index] = 2
        selected_high = random.choice(highest_indexes)
        while selected_high == index:
            selected_high = random.choice(highest_indexes)
        positive_bar = barwise_spec[selected_high]

        lowest_indexes = np.argpartition(this_bar_similarities, medium_thresh)[:medium_thresh]
        # threshed_mat[index,lowest_indexes] = 0
        # threshed_mat[lowest_indexes,index] = 0
        selected_low = random.choice(lowest_indexes)
        negative_bar = barwise_spec[selected_low]
        
        triplet_data.append((bar, positive_bar, negative_bar))
        flatten_triplet_data.append((bar.reshape((vectorized_spec_dim), order="F"), positive_bar.reshape((vectorized_spec_dim), order="F"), negative_bar.reshape((vectorized_spec_dim), order="F")))
    # plot_me_this_spectrogram(threshed_mat)

    triplet_data_loader = torch.utils.data.DataLoader(triplet_data, batch_size=batch_size, num_workers=num_workers)
    flatten_triplet_data_loader = torch.utils.data.DataLoader(flatten_triplet_data, batch_size=batch_size, num_workers=num_workers)
    return triplet_data_loader, flatten_triplet_data_loader
    
# %% Beta-divergence loss
class BetaDivergenceLoss(nn.Module):
    """
    Class defining the Beta divergence loss.
    
    Some inspiration was taken from https://github.com/yoyololicon/pytorch-NMF/blob/master/torchnmf/metrics.py
    """

    def __init__(self, beta = 1, eps = 1e-12):
        """
        Constructor. "eps" is a small contant to avoid dividing by zero.
        """
        super(BetaDivergenceLoss, self).__init__()
        self.beta = beta
        self.eps = eps
        
    def calc_beta_div(self, x1, x2):
        """
        Definition of the beta-divergence.
        """
        if self.beta == 1:
            log_prod = torch.mul(x1, (x1.add(self.eps).log() - x2.add(self.eps).log()))
            return (torch.add(torch.sub(log_prod, x1), x2)).mean()
        elif self.beta == 0:
            x1_div_x2 = torch.div(x1, x2.add(self.eps)).add(self.eps)
            return torch.sub(x1_div_x2, x1_div_x2.log()).sub(1).mean()
        else:
            if self.beta < 0:
                x1 = x1.add(self.eps)
                x2 = x2.add(self.eps)
            elif self.beta < 1:
                x2 = x2.add(self.eps)
            num =  torch.sub(torch.add(x1.pow(self.beta), x2.pow(self.beta).mul(self.beta - 1)), torch.mul(x1, x2.pow(self.beta-1)).mul(self.beta)).mean()
            return num / (self.beta * (self.beta - 1))

    def forward(self, x, y):
        """
        Computation.
        """
        if (x < 0).any():
            raise err.NegativeValuesNotAccepted("Negative values in the input of the network, can't perform beta divergence.")
        if (y < 0).any():
            raise err.NegativeValuesNotAccepted("Negative values in the output of the network, can't perform beta divergence.")
        losses = self.calc_beta_div(x, y)
        return losses.mean()
    