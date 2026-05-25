"""Tests for analysis module."""

import numpy as np
import pytest

from src.analysis import calculate_statistics


def test_calculate_statistics_basic():
    """Test basic statistics calculation."""
    data = np.array([1, 2, 3, 4, 5])
    stats = calculate_statistics(data)

    assert stats["mean"] == 3.0
    assert abs(stats["std"] - np.sqrt(2)) < 1e-10  # np.std uses N, not N-1
    assert stats["min"] == 1
    assert stats["max"] == 5


def test_calculate_statistics_single_value():
    """Test statistics for array with single value."""
    data = np.array([42.0])
    stats = calculate_statistics(data)

    assert stats["mean"] == 42.0
    assert stats["std"] == 0.0
    assert stats["min"] == 42.0
    assert stats["max"] == 42.0


def test_calculate_statistics_negative_values():
    """Test statistics with negative values."""
    data = np.array([-5, -2, 0, 2, 5])
    stats = calculate_statistics(data)

    assert stats["mean"] == 0.0
    assert stats["min"] == -5
    assert stats["max"] == 5


@pytest.mark.parametrize(
    "data,expected_mean",
    [
        (np.array([10.0, 20.0, 30.0]), 20.0),
        (np.array([1, 1, 1]), 1.0),
        (np.array([0, 0, 0, 0]), 0.0),
    ],
)
def test_calculate_statistics_parametrized(data, expected_mean):
    """Parametrized test for various datasets."""
    stats = calculate_statistics(data)
    assert stats["mean"] == expected_mean


def test_calculate_statistics_type_error():
    """Test that TypeError is raised for non-array input."""
    with pytest.raises(TypeError):
        calculate_statistics([1, 2, 3])  # List, not array


def test_calculate_statistics_empty_array():
    """Test that ValueError is raised for empty array."""
    with pytest.raises(ValueError):
        calculate_statistics(np.array([]))


def test_calculate_statistics_return_type():
    """Test that return value is a dictionary with correct keys."""
    data = np.array([1, 2, 3])
    stats = calculate_statistics(data)

    assert isinstance(stats, dict)
    assert set(stats.keys()) == {"mean", "std", "min", "max"}
    assert all(isinstance(v, float) for v in stats.values())
