# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 16:54:59 2020

@author: amarmore
"""

import barmuscomp.model.errors as err

# %% Load everything from as_seg
from as_seg.model.features import *
# See details in as_seg

# %% HCQT
def get_hcqt_params():
    """
    Credit to & al. [1] (comes directly from https://github.com/rabitt/ismir2017-deepsalience)
    
    Fixing parameters for the HCQT computation.

    Returns
    -------
    bins_per_octave : TYPE
        DESCRIPTION.
    n_octaves : TYPE
        DESCRIPTION.
    harmonics : TYPE
        DESCRIPTION.
    sr : TYPE
        DESCRIPTION.
    fmin : TYPE
        DESCRIPTION.
    hop_length : TYPE
        DESCRIPTION.
        
    References
    ----------
    [1] Bittner, R. M., McFee, B., Salamon, J., Li, P., & Bello, J. P. (2017, October). 
    Deep Salience Representations for F0 Estimation in Polyphonic Music. In ISMIR (pp. 63-70).

    """
    bins_per_octave = 60
    n_octaves = 6
    harmonics = [0.5, 1, 2, 3, 4, 5]
    sr = 22050
    fmin = 32.7
    hop_length = 256
    return bins_per_octave, n_octaves, harmonics, sr, fmin, hop_length


def compute_hcqt_bittner(signal, sr):
    """
    Credit to Bittner & al. [1] (comes from https://github.com/rabitt/ismir2017-deepsalience).
    
    Computes HCQT representation of the signal, as presented in [1] (3-rd order tensor).

    Parameters
    ----------
    signal : numpy array
        Signal of the song.
    sr : int
        the sampling_rate

    Returns
    -------
    log_hcqt : np array
        The tensor of logarithm HCQT.
        
    References
    ----------
    [1] Bittner, R. M., McFee, B., Salamon, J., Li, P., & Bello, J. P. (2017, October). 
    Deep Salience Representations for F0 Estimation in Polyphonic Music. In ISMIR (pp. 63-70).
    """
    (bins_per_octave, n_octaves, harmonics,
     sr, f_min, hop_length) = get_hcqt_params()
    #y, fs = librosa.load(audio_fpath, sr=sr)

    cqt_list = []
    shapes = []
    for h in harmonics:
        cqt = librosa.cqt(
            signal, sr=sr, hop_length=hop_length, fmin=f_min*float(h),
            n_bins=bins_per_octave*n_octaves,
            bins_per_octave=bins_per_octave
        )
        cqt_list.append(cqt)
        shapes.append(cqt.shape)

    shapes_equal = [s == shapes[0] for s in shapes]
    if not all(shapes_equal):
        min_time = np.min([s[1] for s in shapes])
        new_cqt_list = []
        for i in range(len(cqt_list)):
            new_cqt_list.append(cqt_list[i][:, :min_time])
        cqt_list = new_cqt_list

    log_hcqt = ((1.0/80.0) * librosa.core.amplitude_to_db(
        np.abs(np.array(cqt_list)), ref=np.max)) + 1.0

    return log_hcqt

def my_compute_hcqt(signal, sr):
    """
    Credit to Bittner & al. [1] (comes from https://github.com/rabitt/ismir2017-deepsalience).
    
    Computes HCQT representation of the signal, as presented in [1] (3-rd order tensor).
    The order of the mode is changed though, so tht first two modes correspond to frequency and time respectively,
    and that the third corresponds to harmonic content.

    Parameters
    ----------
    signal : numpy array
        Signal of the song.
    sr : int
        the sampling_rate

    Returns
    -------
    log_hcqt : np array
        The tensor of logarithm HCQT.
        
    References
    ----------
    [1] Bittner, R. M., McFee, B., Salamon, J., Li, P., & Bello, J. P. (2017, October). 
    Deep Salience Representations for F0 Estimation in Polyphonic Music. In ISMIR (pp. 63-70).
    """
    (bins_per_octave, n_octaves, harmonics, sr, f_min, hop_length) = get_hcqt_params()

    freq_mode_len = bins_per_octave*n_octaves

    first_cqt = librosa.cqt(signal, sr=sr, hop_length=hop_length, fmin=f_min*float(harmonics[0]),
                            n_bins=freq_mode_len, bins_per_octave=bins_per_octave)

    time_mode_len = first_cqt.shape[1]
    
    h_cqt = np.array(first_cqt).reshape(freq_mode_len, time_mode_len, 1)
    
    for h in harmonics[1:]:
        cqt = librosa.cqt(signal, sr=sr, hop_length=hop_length, fmin=f_min*float(h),
            n_bins=bins_per_octave*n_octaves,bins_per_octave=bins_per_octave)
        current_cqt = cqt.reshape(freq_mode_len, time_mode_len, 1)
        h_cqt = np.append(h_cqt, current_cqt, axis = 2)

    log_hcqt = ((1.0/80.0) * librosa.core.amplitude_to_db(np.abs(h_cqt), ref=np.max)) + 1.0

    return log_hcqt

