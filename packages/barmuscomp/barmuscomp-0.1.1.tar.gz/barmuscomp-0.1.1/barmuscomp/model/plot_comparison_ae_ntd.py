# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 15:37:15 2022

@author: amarmore

Plotting functions used for comparing NTD and AE-NTD outputs.
Ugly code.
"""
import as_seg.autosimilarity_computation as as_comp
from barmuscomp.model.current_plot import *
import barmuscomp.model.pattern_study as ps

import numpy as np
import pandas as pd

def plot_audio_diff_ntd_ae_in_dataframe(signal_ntd, signal_ae):
    """
    Listening to both audio examples (comparing NTD and AE-NTD).
    """
    df = pd.DataFrame(np.array([signal_ntd, signal_ae]), index = ["Audio NTD", "Audio AE"])
    for i in range(df.shape[1]):
        df[i] = df[i].T.apply(lambda x:x._repr_html_().replace('\n', '').strip())#, axis=1)
    df_html = df.T.to_html(escape=False, index=False)
    ipd.display(ipd.HTML(df_html))
    
def plot_spec_ntd_ae(spec_1, spec_2, title, to_permute = True, plot_diff = False):
    """
    Plotting both NTD and AE-NTD Q matrix.
    """
    if spec_1.shape[0] == spec_1.shape[1]:
        fig, axs = plt.subplots(1, 2, figsize=(14,7))
    else:
        fig, axs = plt.subplots(1, 2, figsize=(15,min(5, 15*spec_1.shape[0]/spec_1.shape[1])))
    if to_permute:
        permut_1 = permutate_factor(spec_1.T) 
        spec_1 = spec_1[permut_1]
        permut_2 = permutate_factor(spec_2.T)
        spec_2 = spec_2[permut_2]
    diff = spec_2 - spec_1
    axs[0].pcolormesh(np.arange(spec_1.shape[1]), np.arange(spec_1.shape[0]), spec_1, cmap=cm.Greys, shading='auto')
    axs[0].set_title(f"{title} of NTD")
    axs[1].pcolormesh(np.arange(spec_2.shape[1]), np.arange(spec_2.shape[0]), spec_2, cmap=cm.Greys, shading='auto')
    axs[1].set_title(f"{title} of AE")
    axs[0].invert_yaxis()
    axs[1].invert_yaxis()
    plt.show()
    if plot_diff:
        if spec_1.shape[0] == spec_1.shape[1]:
            fig, axs = plt.subplots(1, 2, figsize=(14,7))
        else:
            fig, axs = plt.subplots(1, 2, figsize=(15,min(5, 15*spec_1.shape[0]/spec_1.shape[1])))
        axs[0].pcolormesh(np.arange(diff.shape[1]), np.arange(diff.shape[0]), diff, cmap=cm.Greys, shading='auto')
        axs[0].set_title(f"Diff entre les 2 spectrogrammes\n (couleurs normalisées entre min et max)\n Diff maximale: {np.amax(np.abs(diff))}")
        the_max = max(np.amax(spec_1), np.amax(spec_2))
        axs[1].pcolormesh(np.arange(diff.shape[1]), np.arange(diff.shape[0]), diff, cmap=cm.Greys, vmin=0, vmax=the_max, shading='auto')
        axs[1].set_title(f"Diff entre les 2 spectrogrammes\n (couleurs normalisées entre 0 et max des 2 spectrogrammes)\n Valeur max des 2 specs{the_max}")
        axs[0].invert_yaxis()
        axs[1].invert_yaxis()
        plt.show()

def plot_patterns_ae_and_ntd(spec_patterns_ntd, signal_patterns_ntd, core_ae, factors_ae, signal_patterns_ae, nb_patterns_to_show):
    """
    Compares the patterns of both NTD and AE-NTD.
    """
    for i in range(nb_patterns_to_show):
        pattern = factors_ae[0]@core_ae[:,:,i]@factors_ae[1].T
        plot_spec_ntd_ae(spec_patterns_ntd[i], pattern, title = f"{i}-th pattern in the decoder", to_permute = False)
        plot_audio_diff_ntd_ae_in_dataframe(signal_patterns_ntd[i], signal_patterns_ae[i])
        
def plot_comparison_this_ae_ntd(ssae, projection, hop_length, factors_ntd, tensor_mag_original, tensor_phase_original, nb_bars, phase_retrieval_song, phase_retrieval_patterns,
                                autosimilarity_type = "Cosine", plot_patterns = False, nb_patterns_to_show = 4, subdivision = 96, spec_patterns_ntd = None, signal_patterns_ntd = None):
    """
    Compares the overall outputs of both NTD and AE-NTD.
    """    
    autosimil = as_comp.switch_autosimilarity(projection, similarity_type = autosimilarity_type, normalise = True)
    autosimil_ntd = as_comp.switch_autosimilarity(factors_ntd[2], similarity_type = autosimilarity_type, normalise = True)
    plot_spec_ntd_ae(autosimil_ntd, autosimil, "Autosimilarity", to_permute = False)

    W = ssae.get_W()
    H = ssae.get_H()
    G = ssae.get_G()
    proj_np = np.array(projection)

    plot_spec_ntd_ae(factors_ntd[0], W, title = "W matrix")
    plot_spec_ntd_ae(factors_ntd[1].T, H.T, title = "H matrix")
    plot_spec_ntd_ae(factors_ntd[2].T, proj_np.T, title = "Latent representations")
    song_sdr, patterns_sdr, audio_patterns = ps.sdr_songscale_patternscale_encpasulation(G, [W, H, proj_np], hop_length, tensor_mag_original, tensor_phase_original,
                                                                 nb_bars, phase_retrieval_song, phase_retrieval_patterns, subdivision = subdivision)
    
    print(f"SDR at the song scale: {song_sdr}")
    print(f"SDR at the pattern scale: average = {np.mean(patterns_sdr)}, std = {np.std(patterns_sdr)}")

    if plot_patterns:
        plot_patterns_ae_and_ntd(spec_patterns_ntd, signal_patterns_ntd, G, [W, H, proj_np], signal_patterns_ae = audio_patterns, nb_patterns_to_show = nb_patterns_to_show)