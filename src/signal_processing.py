"""Module for signal processing and transformation."""

import numpy as np


def moving_average(signal: np.ndarray, window_size: int) -> np.ndarray:
    """Apply a moving average filter to a signal.

    Computes the moving average of a signal using a sliding window.
    The window size determines the smoothing effect. Larger windows
    result in more smoothing but lose more detail.

    Args:
        signal: Input signal as a 1D numpy array.
        window_size: Size of the moving window. Must be positive and
                     preferably odd. Should be <= len(signal).

    Returns:
        Smoothed signal as a 1D numpy array of the same length as input.
        The first (window_size - 1) values are handled with shorter windows.

    Raises:
        ValueError: If window_size is not positive.
        TypeError: If signal is not a numpy array.

    Example:
        >>> signal = np.array([1, 2, 3, 4, 5, 6, 7])
        >>> smoothed = moving_average(signal, window_size=3)
        >>> smoothed
        array([1.        , 1.5       , 2.        , 3.        , 4.        ,
               5.        , 6.        ])
    """
    if not isinstance(signal, np.ndarray):
        raise TypeError("Signal must be a numpy array")
    if window_size <= 0:
        raise ValueError("Window size must be positive")

    result = np.convolve(signal, np.ones(window_size) / window_size, mode="same")
    return result


def normalize(signal: np.ndarray) -> np.ndarray:
    """Normalize a signal to zero mean and unit standard deviation.

    Applies z-score normalization (standardization) to the signal.
    The output has mean=0 and std=1, making it scale-invariant.

    Args:
        signal: Input signal as a 1D numpy array.

    Returns:
        Normalized signal as a 1D numpy array.

    Raises:
        TypeError: If signal is not a numpy array.

    Example:
        >>> signal = np.array([1, 2, 3, 4, 5])
        >>> normalized = normalize(signal)
        >>> print(f"Mean: {normalized.mean():.2f}, Std: {normalized.std():.2f}")
        Mean: 0.00, Std: 1.00
    """
    if not isinstance(signal, np.ndarray):
        raise TypeError("Signal must be a numpy array")

    mean = np.mean(signal)
    std = np.std(signal)

    if std == 0:
        return np.zeros_like(signal, dtype=float)  # type: ignore[no-any-return]

    normalized = (signal - mean) / std
    return normalized  # type: ignore[no-any-return]
