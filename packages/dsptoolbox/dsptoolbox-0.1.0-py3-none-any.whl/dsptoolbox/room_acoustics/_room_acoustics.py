"""
Low-level methods for room acoustics
"""
import numpy as np


def _reverb(h, fs_hz, mode, ir_start: int = None,
            return_ir_start: bool = False):
    """Computes reverberation time of signal.

    Parameters
    ----------
    h : `np.ndarray`
        Time series.
    fs_hz : int
        Sampling rate in Hz.
    mode : str
        Parameter for the reverberation time.
    ir_start : int, optional
        When not `None`, the index is used as the start of the impulse
        response. Default: `None`.
    return_ir_start : bool, optional
        When `True`, it returns not only reverberation time but also the
        index of the sample with the start of the impulse response.
        Default: `False`.

    Returns
    -------
    float
        Reverberation time in seconds.
    int
        Index of the start of the RIR. Only returned when
        `return_ir_start = True`.

    References
    ----------
    Regarding start of RIR: ISO 3382-1:2009-10, Acoustics - Measurement of
    the reverberation time of rooms with reference to other
    acoustical parameters. pp. 22.

    """
    # Energy decay curve
    energy_curve = h**2
    epsilon = 1e-20
    if ir_start is None:
        max_ind = _find_ir_start(h, threshold_db=-20)
    else:
        max_ind = ir_start
    edc = np.sum(energy_curve) - np.cumsum(energy_curve)
    edc[edc <= 0] = epsilon
    edc = 10*np.log10(edc / edc[max_ind])
    # Reverb
    i1 = np.where(edc < -5)[0][0]
    if mode.casefold() == 'T20'.casefold():
        i2 = np.where(edc < -25)[0][0]
    elif mode.casefold() == 'T30'.casefold():
        i2 = np.where(edc < -35)[0][0]
    elif mode.casefold() == 'T60'.casefold():
        i2 = np.where(edc < -65)[0][0]
    elif mode.casefold() == 'EDT'.casefold():
        i1 = np.where(edc < 0)[0][0]
        i2 = np.where(edc < -10)[0][0]
    else:
        raise ValueError('Supported modes are only T20, T30, T60 and EDT')
    # Time
    length_samp = i2 - i1
    time = np.linspace(0, length_samp/fs_hz, length_samp)
    reg = np.polyfit(time, edc[i1:i2], 1)
    if return_ir_start:
        return (60 / np.abs(reg[0])), ir_start
    return (60 / np.abs(reg[0]))


def _find_ir_start(ir, threshold_db=-20):
    """Find start of an IR using a threshold. Done for 1D-arrays.

    """
    energy_curve = ir**2
    epsilon = 1e-20
    energy_curve_db = 10*np.log10(energy_curve / max(energy_curve)
                                  + epsilon)
    return np.arange(len(energy_curve_db))[energy_curve_db > threshold_db][0]


def _complex_mode_identification(spectra: np.ndarray, n_functions: int = 1):
    """Complex transfer matrix and CMIF from:
    http://papers.vibetech.com/Paper17-CMIF.pdf

    Parameters
    ----------
    spectra : `np.ndarray`
        Matrix containing spectra of the necessary IR.
    n_functions : int, optional
        Number of singular value vectors to be returned. Default: 1.

    Returns
    -------
    cmif : `np.ndarray`
        Complex mode identificator function (matrix).

    References
    ----------
    http://papers.vibetech.com/Paper17-CMIF.pdf

    """
    assert n_functions <= spectra.shape[1], f'{n_functions} is too many ' +\
        f'functions for spectra of shape {spectra.shape}'

    n_rir = spectra.shape[1]
    H = np.zeros((n_rir, n_rir, spectra.shape[0]), dtype='cfloat')
    for n in range(n_rir):
        H[0, n, :] = spectra[:, n]
        H[n, 0, :] = spectra[:, n]  # Conjugate?!
    cmif = np.empty((spectra.shape[0], n_functions))
    for ind in range(cmif.shape[0]):
        v, s, u = np.linalg.svd(H[:, :, ind])
        for nf in range(n_functions):
            cmif[ind, nf] = s[nf]
    return cmif


def _sum_magnitude_spectra(magnitudes: np.ndarray):
    """np.sum of all magnitude spectra

    Parameters
    ----------
    magnitudes : `np.ndarray`
        The magnitude spectra. If complex, it is assumed to be the spectra.

    Returns
    -------
    summed : `np.ndarray`
        np.sum of magnitude spectra.

    """
    if np.iscomplexobj(magnitudes):
        magnitudes = abs(magnitudes)
    summed = np.sum(magnitudes, axis=1)
    return summed
