# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 16:29:17 2019

@author: amarmore

Defining common plotting functions.

NB: This module's name actually comes from an incorrect translation
from the french "courant" into "current", instead of "common".
Please excuse me for this translation.
"""

import as_seg.autosimilarity_computation as as_comp

from sklearn.decomposition import PCA
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import pandas as pd
import IPython.display as ipd

# %% Load everything from as_seg
from as_seg.model.current_plot import *

# %% NTD specific
def plot_me_this_tucker(factors, core, cmap = cm.Greys):
    """
    Plot all factors, and each slice of the core (as musical pattern) from the NTD.
    """
    plot_me_this_spectrogram(factors[0], title = "Midi factor", x_axis = "Atoms", y_axis = "Midi value", invert_y_axis = False, cmap = cmap)
    plot_me_this_spectrogram(factors[1].T, title = "Rythmic patterns factor", x_axis = "Position in bar", y_axis = "Atoms", cmap = cmap)
    plot_me_this_spectrogram(factors[2].T, title = "Structural patterns factor", x_axis = "Bar index", y_axis = "Atoms", cmap = cmap)
    print("Core:")
    for i in range(len(core[0,0,:])):
        plot_me_this_spectrogram(core[:,:,i], title = "Core, slice " + str(i), x_axis = "Time atoms", y_axis = "Freq Atoms", cmap = cmap)

def permutate_factor(factor):
    """
    Computes the permutation of columns of the factors for them to be visually more comprehensible.
    """
    permutations = []
    for i in factor:
        idx_max = np.argmax(i)
        if idx_max not in permutations:
            permutations.append(idx_max)
    for i in range(factor.shape[1]):
        if i not in permutations:
            permutations.append(i)
    return permutations

def plot_permuted_factor(factor, title = None,x_axis = None, y_axis = None, cmap = cm.Greys):
    """
    Plots this factor, but permuted to be easier to understand visually.
    """
    permut = permutate_factor(factor)
    plot_me_this_spectrogram(factor.T[permut], title = title,x_axis = x_axis, y_axis = y_axis,
                             figsize=(factor.shape[0]/10,factor.shape[1]/10), cmap = cmap)

def plot_permuted_tucker(factors, core, cmap = cm.Greys, plot_core = True):
    """
    Plots every factor and slice of the core from the NTD, but permuted to be easier to understand visually.
    """
    plot_me_this_spectrogram(factors[0], title = "W matrix (muscial content)",
                         x_axis = "Atoms", y_axis = "Pitch-class Index", cmap = cmap)
    h_permut = permutate_factor(factors[1])
    plot_me_this_spectrogram(factors[1].T[h_permut], title = "H matrix: time at barscale (rythmic content)",
                             x_axis = "Position in the bar\n(in frame indexes)", y_axis = "Atoms\n(permuted for\nvisualization purpose)", 
                             figsize=(factors[1].shape[0]/10,factors[1].shape[1]/10), cmap = cmap)
    q_permut = permutate_factor(factors[2])
    plot_me_this_spectrogram(factors[2].T[q_permut], title = "Q matrix: Bar content feature",
                             x_axis = "Index of the bar", y_axis = "Musical pattern index\n(permuted for\nvisualization purpose)", 
                             figsize=(factors[2].shape[0]/10,factors[2].shape[1]/10), cmap = cmap)
    if plot_core:
        for i, idx in enumerate(q_permut):
            plot_me_this_spectrogram(core[:,h_permut,idx], title = "Core, slice {} (slice {} in original decomposition order)".format(i, idx), x_axis = "Time atoms", y_axis = "Freq Atoms", cmap = cm.Greys)
  

# %% Plotting audio files, in order to listen to them
def plot_audio_list_in_dataframe(audios_list):
    """
    Print this list of audio signals in a list.
    """
    #Never tested, tocheck
    df = pd.DataFrame(np.array(audios_list), columns = ["All patterns"]).T
    #df[0] = df[0].apply(lambda x:x._repr_html_().replace('\n', '').strip())#, axis=1)
    for i in range(df.shape[1]):
        df[i] = df[i].T.apply(lambda x:x._repr_html_().replace('\n', '').strip())#, axis=1)
    df_html = df.T.to_html(escape=False, index=False)
    ipd.display(ipd.HTML(df_html))
    
# %% Single-Song AutoEncoders specific
def plot_latent_space(latent_vectors, labels = None):
    """
    Visualization of the latent projection, as the matrix of representation, and as both autosimilarity and PCA of latent vectors.

    Parameters
    ----------
    latent_vectors : array
        Concatenation of the latent vectors, or matrix of latent representations. 
        (same mathematical meaning but can be of different computation types.)
    labels : None or array, optional
        If labels are set, they will be used to color the output of PCA projection.
        If they are set to None, no label is used. The default is None.

    Returns
    -------
    None, but plots latent visualizations.

    """
    np_lv = np.array(latent_vectors)
    plot_me_this_spectrogram(np_lv.T, figsize=(np_lv.shape[0]/5,np_lv.shape[1]/5), title = "z matrix", x_axis = "Bar index", y_axis = "Latent space")
    
    fig, axs = plt.subplots(1, 2, figsize=(15,7))

    autosimil = as_comp.switch_autosimilarity(latent_vectors, similarity_type = "cosine", normalise = True)
    padded_autosimil = pad_factor(autosimil)
    axs[0].pcolormesh(np.arange(padded_autosimil.shape[1]), np.arange(padded_autosimil.shape[0]), padded_autosimil, cmap = cm.Greys)
    axs[0].set_title('Autosimilarity of the z (projection in latent space)')
    axs[0].invert_yaxis()
    axs[0].set_xlabel("Bar index")
    axs[0].set_ylabel("Bar index")
    
    if np_lv.shape[1] == 2:
        if not isinstance(labels,np.ndarray) and labels == None:
            axs[1].scatter(np_lv[:,0],np_lv[:,1])
        else:
            axs[1].scatter(np_lv[:,0],np_lv[:,1], c=labels)
    else:
        pca = PCA(n_components=2)
        principalComponents = pca.fit_transform(np_lv)
        if not isinstance(labels,np.ndarray) and labels == None:
            axs[1].scatter(principalComponents[:,0],principalComponents[:,1])
        else:
            axs[1].scatter(principalComponents[:,0],principalComponents[:,1], c=labels)

    axs[1].set_title('PCA of the z (projection in the latent space)')
    plt.show()

# %% AE-NTD
def plot_audio_diff_ntd_ae_in_dataframe(signal_ntd, signal_ae):
    df = pd.DataFrame(np.array([signal_ntd, signal_ae]), index = ["Audio NTD", "Audio AE"])
    for i in range(df.shape[1]):
        df[i] = df[i].T.apply(lambda x:x._repr_html_().replace('\n', '').strip())#, axis=1)
    df_html = df.T.to_html(escape=False, index=False)
    ipd.display(ipd.HTML(df_html))
    
    import pandas as pd
import IPython.display as ipd

def plot_audio_diff_beta_in_dataframe(signal_beta2, signal_beta1, signal_beta0):
    """
    Plots the different reconstruction with different beta values in a dataframe.
    Hardcoded for Beta = 2, 1 and 0.
    """
    df = pd.DataFrame(np.array([signal_beta2, signal_beta1, signal_beta0]), index = ["beta = 2", "beta = 1", "beta = 0"])
    #df[0] = df[0].apply(lambda x:x._repr_html_().replace('\n', '').strip())#, axis=1)
    for i in range(df.shape[1]):
        df[i] = df[i].T.apply(lambda x:x._repr_html_().replace('\n', '').strip())#, axis=1)
    df_html = df.T.to_html(escape=False, index=False)
    ipd.display(ipd.HTML(df_html))


