# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 17:34:39 2020

@author: amarmore

"""

import as_seg.data_manipulation as dm
import barmuscomp.ae as ae
import barmuscomp.model.errors as err
import barmuscomp.scripts.default_path as paths
import nn_fac.ntd as NTD

import os
import numpy as np

# %% Load everything from as_seg
from as_seg.scripts.overall_scripts import *

# %% NTD specific
def NTD_decomp_as_script(persisted_path, persisted_arguments, tensor_spectrogram, ranks, init = "tucker", update_rule = "hals", beta = None, compute_if_not_persisted = True): 
    """
    Computes the NTD from the tensor_spectrogram and with specified ranks.
    On the first hand, if the NTD is persisted, it will load and return its results.
    If it's not, it will compute the NTD, store it, and return it.

    Parameters
    ----------
    persisted_path : String
        Path of the persisted decompositions and bars.
    persisted_arguments : String
        Identifier of the specific NTD to load/save.
    tensor_spectrogram : tensorly tensor
        The tensor to decompose.
    ranks : list of integers
        Ranks of the decomposition.
    init : String, optional
        The type of initialization of the NTD.
        See the NTD module to have more information regarding initialization.
        The default is "chromas",
        meaning that the first factor will be set to the 12-size identity matrix,
        and the other factors will be initialized by HOSVD.

    Raises
    ------
    NotImplementedError
        Errors in the arguments.

    Returns
    -------
    core : tensorly tensor
        The core of the decomposition.
    factors : numpy array
        The factors of the decomposition.

    """
    if update_rule == "hals":
        path_for_ntd = "{}/ntd/{}_{}_{}".format(persisted_path, ranks[0], ranks[1], ranks[2])
    elif update_rule == "mu":
        path_for_ntd = "{}/ntd_mu/{}_{}_{}".format(persisted_path, ranks[0], ranks[1], ranks[2])
    else:
        raise NotImplementedError(f"Update rule type not understood: {update_rule}")
    
    if update_rule == "mu" and beta == None:
        raise NotImplementedError("Inconsistent arguments. Beta should be set if the update_rule is the MU.")
        
    try:
        a_core_path = "{}/core{}.npy".format(path_for_ntd, persisted_arguments)
        a_core = np.load(a_core_path)
        a_factor_path = "{}/factors{}.npy".format(path_for_ntd, persisted_arguments)
        a_factor = np.load(a_factor_path, allow_pickle=True)
        return a_core, a_factor
    except FileNotFoundError:
        assert compute_if_not_persisted
        if update_rule == "hals":
            core, factors = NTD.ntd(tensor_spectrogram, ranks = ranks, init = init, verbose = False,
                                sparsity_coefficients = [None, None, None, None], normalize = [True, True, False, True], mode_core_norm = 2,
                                deterministic = True)
        elif update_rule == "mu":
            core, factors = NTD.ntd_mu(tensor_spectrogram, ranks = ranks, init = init, verbose = False, beta = beta, n_iter_max=1000,
                                sparsity_coefficients = [None, None, None, None], normalize = [True, True, False, True], mode_core_norm = 2,
                                deterministic = True)
        
        pathlib.Path(path_for_ntd).mkdir(parents=True, exist_ok=True)
    
        core_path = "{}/core{}".format(path_for_ntd, persisted_arguments)
        np.save(core_path, core)
        factors_path = "{}/factors{}".format(path_for_ntd, persisted_arguments)
        np.save(factors_path, factors)
        return core, factors
    
# %% SSAE specific 
def load_or_save_convolutional_projection(persisted_path, song_name, data_loader, dim_latent_space, lr = 1e-3, n_epochs = 1000, feature = "pcp", hop_length = 32, subdivision_bars = 96, freq_len = 12, compute_if_not_persisted = True):
    """
    Loads the neural network projection for this song, which was persisted after its computation.

    Parameters
    ----------
    persisted_path : string
        Path of the folder where the projections should be found.
    song_name : int or string
        Identifier of the song.
    data_loader : torch.DataLoader
        The DataLoader associated with the barwise tensor of this song.
    dim_latent_space : int
        Dimension of the latent space.
    sparsity_lambda : None or float
        The sparisty ponderation parameter.
        If set to None, no sparsity is enforced.
    nn : boolean, optional
        DEPRECATED. Whether the latent vectors should be nonnegative or not. 
        Accepted behavior nowadays is not enforcing nonnegativity. The default is False.
    lr : float, optional
        Learning rate of the network. The default is 1e-3.
    n_epochs : int, optional
        Number of epochs to perform. The default is 1000.
    norm_tensor : float, optional
        Norm of the barwise tensor. Used to noramlize the sparsity parameter, so useless when sparsity lambda is set to None.
        The default is None.
    feature : string, optional
        The feature used to represent the song. See model.feature.py for details. The default is "pcp".
    hop_length : int, optional
        Hop_length used to compute the original spectrogram. The default is 32.
    subdivision_bars : int, optional
        The number of subdivision of the bar to be contained in each slice of the tensor.
    freq_len : int, optional
        Dimension of the frequency mode (frequency-related representation of music). The default is 12.
    compute_if_not_persisted : boolean, optional
        Indicating hether the network should be computed if it's not found in persisted networks.
        Should be set to True if networks are computed for the first time, and to False to speed up computation in tests where they have already been computed.
        The default is True.

    Raises
    ------
    FileNotFoundError
        If the network asn't found and if ``FileNotFoundError'' is set to False.

    Returns
    -------
    projection : numpy array
        Latent projection of each bar through this network.

    """
    persisted_params = "song{}_feature{}_hop{}_subdivbars{}_initkaiming_lr{}_nepochs{}".format(song_name, feature, hop_length, subdivision_bars, lr, n_epochs)
    
    conv_save_name = "{}/neural_nets/conv_4_16_k3_transk3_latentfc{}_{}".format(persisted_path, dim_latent_space, persisted_params)
    conv_load_name = "{}/neural_nets/transfered/conv_4_16_k3_transk3_latentfc{}_{}".format(persisted_path, dim_latent_space, persisted_params)
    
    try:
        projection = np.load("{}.npy".format(conv_load_name), allow_pickle = True)
    except FileNotFoundError:
        try:
            projection = np.load("{}.npy".format(conv_save_name), allow_pickle = True)
        except FileNotFoundError:
            if compute_if_not_persisted:
                conv_model = ae.ConvolutionalAutoencoder(input_size_x = subdivision_bars, input_size_y = freq_len, dim_latent_space = dim_latent_spaces)
                conv_model = conv_model.my_optim_method(n_epochs, data_loader, lr=lr, verbose = False, labels = None)
                projection = conv_model.get_latent_projection(data_loader)
                np.save(conv_save_name, projection)
            else:
                raise FileNotFoundError(f"Neural network projection not found, check the name: {conv_save_name}") from None

    return projection