"""Tests for data_loader module."""

import os
import tempfile

import pandas as pd
import pytest

from src.data_loader import load_csv


@pytest.fixture
def sample_csv_file():
    """Create a temporary CSV file for testing."""
    with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False) as f:
        f.write("time,signal\n")
        f.write("0,10.5\n")
        f.write("1,11.2\n")
        f.write("2,10.8\n")
        temp_path = f.name

    yield temp_path

    os.unlink(temp_path)


def test_load_csv_success(sample_csv_file):
    """Test successful loading of a valid CSV file."""
    df = load_csv(sample_csv_file)

    assert isinstance(df, pd.DataFrame)
    assert df.shape == (3, 2)
    assert list(df.columns) == ["time", "signal"]


def test_load_csv_content(sample_csv_file):
    """Test that loaded CSV content is correct."""
    df = load_csv(sample_csv_file)

    assert df.iloc[0]["time"] == 0
    assert df.iloc[0]["signal"] == 10.5
    assert df.iloc[2]["signal"] == 10.8


def test_load_csv_file_not_found():
    """Test that FileNotFoundError is raised for non-existent file."""
    with pytest.raises(FileNotFoundError):
        load_csv("/nonexistent/path/file.csv")


def test_load_csv_invalid_format():
    """Test that ParserError is raised for invalid CSV format."""
    with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False) as f:
        f.write("invalid\ndata\nformat\x00\n")
        temp_path = f.name

    try:
        with pytest.raises(pd.errors.ParserError):
            load_csv(temp_path)
    finally:
        os.unlink(temp_path)
