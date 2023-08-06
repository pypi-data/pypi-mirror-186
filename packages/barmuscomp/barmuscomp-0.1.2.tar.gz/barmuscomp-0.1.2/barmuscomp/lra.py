# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 18:47:32 2022

@author: amarmore

Multilinear (NTD) and Linear (PCA and NMF) barwise compression schemes.

All fused under the term "low-rank approximations".

See [1 - Chapter 4] or [2] for details on NTD, and [1, Chap 5.3] or [3] for details about PCA and NMF.

References
----------
[1] Unsupervised Machine Learning Paradigms for the Representation of Music Similarity and Structure, 
PhD Thesis Marmoret Axel 
(not uploaded yet but will be soon!)
(You should check the website hal.archives-ouvertes.fr/ in case this docstring is not updated with the reference.)

[2] Marmoret, A., Cohen, J., Bertin, N., & Bimbot, F. (2020, October). 
Uncovering Audio Patterns in Music with Nonnegative Tucker Decomposition for Structural Segmentation. 
In ISMIR 2020-21st International Society for Music Information Retrieval (pp. 1-7).

[3] Marmoret, A., Cohen, J.E, and Bimbot, F., "Barwise Compression Schemes 
for Audio-Based Music Structure Analysis"", in: 19th Sound and Music Computing Conference, 
SMC 2022, Sound and music Computing network, 2022.
"""

import as_seg.barwise_input as bi

import nn_fac.nmf as NMF
import nn_fac.ntd as NTD

from sklearn.decomposition import PCA
from sklearn.decomposition import KernelPCA
import numpy as np

# %% NTD
def get_ntd_projection(spectrogram, core_dimensions, bars, 
                       beta = 2, init = "tucker", 
                       subdivision_bars = 96, hop_length = 32, sampling_rate = 44100):
    """
    Return the Q matrix of NTD (barwise projection).

    Parameters
    ----------
    spectrogram : list of list of floats or numpy array
        The spectrogram to analyze, barwise.
    core_dimensions : list of integers
        The dimensions for each mode of the core tensor (number of columns for each factor).
    bars : list of tuples
        List of the bars (start, end), in seconds, to cut the spectrogram at bar delimitation.
    beta: float
        The beta parameter for the beta-divergence.
        Particular cases:
            2 - Euclidean norm
            1 - Kullback-Leibler divergence
            0 - Itakura-Saito divergence
        Default: 2
    init: "random" | "tucker" | "chromas" |
        - If set to random:
            Initializes with random factors of the correct size.
            The randomization is the uniform distribution in [0,1),
            which is the default from numpy random.
        - If set to tucker:
            Resolve a tucker decomposition of the tensor T (by HOSVD) and
            initializes the factors and the core as this resolution, clipped to be nonnegative.
            The tucker decomposition is performed with tensorly [3].
        - If set to "chromas":
            Resolve a tucker decomposition of the tensor T (by HOSVD) and
            initializes the factors and the core as this resolution, clipped to be nonnegative.
            The tucker decomposition is performed with tensorly [3].
            Contrary to "tucker" init, the first factor will then be set to the 12-size identity matrix,
            because it's a decomposition model specific for modeling music expressed in chromas.
        Default: tucker
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
        Compressed matrix, of size (bars, compression_dimension).

    """
    tensor_spectrogram = bi.tensorize_barwise_FTB(spectrogram, bars, hop_length/sampling_rate, subdivision_bars)
    _, factors = ntd_computation(tensor_spectrogram, core_dimensions, beta, init)
    return factors[2]

def ntd_computation(tensor_spectrogram, core_dimensions, beta = 2, init = "tucker"):
    """
    Computed the NTD on the given tensor_spectrogram.

    Parameters
    ----------
    tensor_spectrogram : tensorly tensor
        The tensor-spectrogram on which should be performed NTD.
    core_dimensions : list of integers
        The dimensions for each mode of the core tensor (number of columns for each factor).
    beta: float
        The beta parameter for the beta-divergence.
        Particular cases:
            2 - Euclidean norm
            1 - Kullback-Leibler divergence
            0 - Itakura-Saito divergence
        Default: 2
    init: "random" | "tucker" | "chromas" |
        - If set to random:
            Initializes with random factors of the correct size.
            The randomization is the uniform distribution in [0,1),
            which is the default from numpy random.
        - If set to tucker:
            Resolve a tucker decomposition of the tensor T (by HOSVD) and
            initializes the factors and the core as this resolution, clipped to be nonnegative.
            The tucker decomposition is performed with tensorly [3].
        - If set to "chromas":
            Resolve a tucker decomposition of the tensor T (by HOSVD) and
            initializes the factors and the core as this resolution, clipped to be nonnegative.
            The tucker decomposition is performed with tensorly [3].
            Contrary to "tucker" init, the first factor will then be set to the 12-size identity matrix,
            because it's a decomposition model specific for modeling music expressed in chromas.
        Default: tucker

    Returns
    -------
    core: tensorly tensor
        The core tensor linking the factors of the decomposition
    factors: numpy
        An array containing all the factors computed with the NTD

    """
    if beta == 2:
        core, factors = NTD.ntd(tensor_spectrogram, ranks = core_dimensions, init = init, verbose = False,
                            sparsity_coefficients = [None, None, None, None], normalize = [True, True, False, True], mode_core_norm = 2,
                            deterministic = True)
    else:
        core, factors = NTD.ntd_mu(tensor_spectrogram, ranks = core_dimensions, init = init, verbose = False, beta = beta, n_iter_max=1000,
                            sparsity_coefficients = [None, None, None, None], normalize = [True, True, False, True], mode_core_norm = 2,
                            deterministic = True)
    return core, factors

# %% PCA
def get_pca_projection(spectrogram, compression_dimension, bars, 
                       subdivision_bars = 96, hop_length = 32, sampling_rate = 44100):
    """
    Returns the PCA projection of this spectrogram.

    Parameters
    ----------
    spectrogram : list of list of floats or numpy array
        The spectrogram to analyze, barwise.
    compression_dimension : positive integer
        Dimension of compression (number of principal components to keep).
    bars : list of tuples
        List of the bars (start, end), in seconds, to cut the spectrogram at bar delimitation.
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
        Compressed matrix, of size (bars, compression_dimension).

    """
    barwise_tf_matrix = bi.barwise_TF_matrix(spectrogram, bars, hop_length/sampling_rate, subdivision_bars)
    return pca_projection(barwise_tf_matrix, compression_dimension)
    
def pca_projection(barwise_tf_matrix, compression_dimension):
    """
    Computes the PCA projection of a Barwise TF matrix 
    (matrix where one mode is the different bars in the song, 
     and the other is the vectorization of both the frequency and the time at barscale).
    
    The idea is to compress each bar with PCA, summing up the content.

    Parameters
    ----------
    barwise_tf_matrix : numpy array
        Barwise TF matrix.
    compression_dimension : positive integer
        Dimension of compression (number of principal components to keep).

    Returns
    -------
    numpy array
        Compressed matrix, of size (bars, compression_dimension).

    """
    if compression_dimension > barwise_tf_matrix.shape[0]:
        return pca_projection(barwise_tf_matrix, barwise_tf_matrix.shape[0])
    pca = PCA(n_components=compression_dimension)
    pca_spec = pca.fit(barwise_tf_matrix)
    return pca_spec.transform(barwise_tf_matrix)

def kernel_pca_projection(barwise_tf_matrix, compression_dimension, gamma, kernel='rbf'):
    """
    Projection with Kernel PCA instead of PCA (see scikit_learn() documentation).
    """
    k_pca = KernelPCA(eigen_solver = 'arpack', n_components=compression_dimension, kernel=kernel, gamma = gamma)
    return k_pca.fit_transform(barwise_tf_matrix)

# %% NMF
def get_nmf_projection(spectrogram, compression_dimension, bars, 
                       beta = 2, init = "nndsvd", 
                       subdivision_bars = 96, hop_length = 32, sampling_rate = 44100):
    """
    Returns the NMF projection of this spectrogram.

    Parameters
    ----------
    spectrogram : list of list of floats or numpy array
        The spectrogram to analyze, barwise.
    compression_dimension : positive integer
        Dimension of compression (number of principal components to keep).
    bars : list of tuples
        List of the bars (start, end), in seconds, to cut the spectrogram at bar delimitation.
    beta: float
        The beta parameter for the beta-divergence.
        Particular cases:
            2 - Euclidean norm
            1 - Kullback-Leibler divergence
            0 - Itakura-Saito divergence
        Default: 2
    init: "random" | "nndsvd" |
        - If set to random:
            Initialize with random factors of the correct size.
            The randomization is the uniform distribution in [0,1),
            which is the default from numpy random.
        - If set to nnsvd:
            Corresponds to a Nonnegative Double Singular Value Decomposition
            (NNDSVD) initialization, which is a data based initialization,
            designed for NMF. See [2] for details.
            This NNDSVD if performed via the nimfa toolbox [3].
        Default: nndsvd
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
        Compressed matrix, of size (bars, compression_dimension).

    """
    barwise_tf_matrix = bi.barwise_TF_matrix(spectrogram, bars, hop_length/sampling_rate, subdivision_bars)
    return nmf_computation(barwise_tf_matrix, compression_dimension, beta = beta, init = init)[0]

def nmf_computation(barwise_tf_matrix, compression_dimension, beta = 2, init = "nndsvd"):
    """
    Computes the Barwise NMF, on the Barwise TF matrix. Returns only the compressed representations.
    
    The idea is to compress each bar with NMF, summing up the content.
    
    See nn_fac.nmf() for details.

    Parameters
    ----------
    barwise_tf_matrix : numpy array
        Barwise TF matrix.
    compression_dimension : positive integer
        Dimension of compression (number of principal components to keep).
    beta: float
        The beta parameter for the beta-divergence.
        Particular cases:
            2 - Euclidean norm
            1 - Kullback-Leibler divergence
            0 - Itakura-Saito divergence
        Default: 2
    init: "random" | "nndsvd" | "custom" |
        - If set to random:
            Initialize with random factors of the correct size.
            The randomization is the uniform distribution in [0,1),
            which is the default from numpy random.
        - If set to nnsvd:
            Corresponds to a Nonnegative Double Singular Value Decomposition
            (NNDSVD) initialization, which is a data based initialization,
            designed for NMF. See [2] for details.
            This NNDSVD if performed via the nimfa toolbox [3].
        - If set to custom:
            U_0 and V_0 (see below) will be used for the initialization
        Default: random

    Returns
    -------
    W_nmf : numpy array
        The barwise compressed representaiton with NMF.

    """
    if beta == 2:
        W_nmf, H_nmf = NMF.nmf(barwise_tf_matrix, compression_dimension, update_rule = "hals", beta = 2, init = init, return_costs = False, deterministic = True)
    else:
        W_nmf, H_nmf = NMF.nmf(barwise_tf_matrix, compression_dimension, update_rule = "mu", beta = beta, init = init, return_costs = False, deterministic = True)
    return W_nmf, H_nmf