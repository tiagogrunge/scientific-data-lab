"""Module for loading and validating experimental data."""

import pandas as pd


def load_csv(path: str) -> pd.DataFrame:
    """Load a CSV file into a pandas DataFrame.

    Reads a CSV file from the specified path and returns it as a DataFrame.
    Assumes the first row contains column headers.

    Args:
        path: Path to the CSV file to load.

    Returns:
        DataFrame containing the loaded data.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        pd.errors.ParserError: If the CSV file is malformed.

    Example:
        >>> df = load_csv('sample_data/experiment_001.csv')
        >>> print(df.shape)
        (30, 2)
        >>> print(df.head())
           time  signal
        0     0     10.5
        1     1     11.2
        2     2     10.8
        ...
    """
    try:
        df = pd.read_csv(path, engine='python', on_bad_lines='error')

        # Validate that all rows have the expected number of columns
        expected_cols = len(df.columns)
        with open(path) as f:
            for idx, line in enumerate(f):
                if idx == 0:
                    continue  # Skip header
                col_count = len(line.strip().split(','))
                if col_count != expected_cols:
                    raise pd.errors.ParserError(
                        f"Row {idx + 1} has {col_count} columns, expected {expected_cols}"
                    )

        return df
    except FileNotFoundError as e:
        raise FileNotFoundError(f"File not found: {path}") from e
    except pd.errors.ParserError:
        raise
    except Exception as e:
        raise pd.errors.ParserError(f"Error parsing CSV file: {path}") from e
