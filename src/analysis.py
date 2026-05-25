"""Module for statistical analysis of experimental data."""

import numpy as np


def calculate_statistics(data: np.ndarray) -> dict:
    """Calculate descriptive statistics for a dataset.

    Computes common statistical measures for the input data.
    Returns a dictionary containing mean, standard deviation,
    minimum and maximum values.

    Args:
        data: Input data as a 1D numpy array.

    Returns:
        Dictionary with the following keys:
            - 'mean': Arithmetic mean of the data
            - 'std': Standard deviation
            - 'min': Minimum value
            - 'max': Maximum value

    Raises:
        TypeError: If data is not a numpy array.
        ValueError: If data is empty.

    Example:
        >>> data = np.array([1, 2, 3, 4, 5])
        >>> stats = calculate_statistics(data)
        >>> print(stats)
        {'mean': 3.0, 'std': 1.41..., 'min': 1, 'max': 5}
    """
    if not isinstance(data, np.ndarray):
        raise TypeError("Data must be a numpy array")
    if data.size == 0:
        raise ValueError("Data array cannot be empty")

    statistics = {
        "mean": float(np.mean(data)),
        "std": float(np.std(data)),
        "min": float(np.min(data)),
        "max": float(np.max(data)),
    }

    return statistics
