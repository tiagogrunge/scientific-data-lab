"""Module for data visualization."""

import numpy as np
import matplotlib.pyplot as plt


def plot_signal(data: np.ndarray, title: str = "Signal") -> None:
    """Plot a 1D signal using matplotlib.

    Creates a simple line plot of the signal. The x-axis represents
    the sample index and the y-axis represents the signal values.

    Args:
        data: 1D numpy array containing signal values to plot.
        title: Title for the plot. Defaults to "Signal".

    Raises:
        TypeError: If data is not a numpy array.
        ValueError: If data is not 1D.

    Example:
        >>> signal = np.sin(np.linspace(0, 2*np.pi, 100))
        >>> plot_signal(signal, title="Sine Wave")
    """
    if not isinstance(data, np.ndarray):
        raise TypeError("Data must be a numpy array")
    if data.ndim != 1:
        raise ValueError("Data must be a 1D array")

    plt.figure(figsize=(10, 6))
    plt.plot(data, linewidth=2)
    plt.title(title, fontsize=14, fontweight="bold")
    plt.xlabel("Sample Index", fontsize=12)
    plt.ylabel("Signal Value", fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()
