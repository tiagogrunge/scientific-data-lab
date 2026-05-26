# Scientific Data Lab

## Purpose

The **Scientific Data Lab** is a collaborative learning project focused on:

- 🐍 **Python for scientific data** - Learn to process, analyze, and visualize experimental data
- 🔗 **Git and collaboration** - Practice Git, Pull Requests, and code review in an educational environment
- ✅ **Software quality** - Learn about unit tests, CI/CD, type hints, and linting
- 🧪 **Engineering best practices** - Structure prepared to evolve into scientific instrumentation systems like NICOS

## Project Structure

```
scientific-data-lab/
├── README.md                 # This file
├── docs/                     # Documentation
│   ├── roadmap.md           # Learning roadmap
│   ├── architecture.md       # System architecture
│   └── learning-notes/       # Learning notes
├── src/                      # Main source code
│   ├── __init__.py
│   ├── data_loader.py        # Data loading
│   ├── signal_processing.py  # Signal processing
│   ├── analysis.py           # Statistical analysis
│   └── visualization.py      # Data visualization
├── tests/                    # Unit tests
│   ├── __init__.py
│   ├── test_loader.py
│   └── test_analysis.py
├── sample_data/              # Sample data
│   └── experiment_001.csv
├── notebooks/                # Jupyter notebooks
│   └── exploration.ipynb
├── .github/                  # GitHub configuration
│   └── workflows/
│       └── ci.yml            # CI/CD pipeline
├── requirements.txt          # Python dependencies
├── .gitignore                # Files to ignore in Git
└── pyproject.toml            # Tools configuration
```

## Quick Start

### 1. Set up virtual environment

```bash
# Create virtual environment
python -m venv .venv

# Activate (Linux/macOS)
source .venv/bin/activate

# Activate (Windows)
.venv\Scripts\activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 2.5. Configure Git commit template (optional)

To use the conventional commit template automatically:

```bash
git config commit.template .gitmessage
```

Or globally for all repositories:

```bash
git config --global commit.template /path/to/scientific-data-lab/.gitmessage
```

### 3. Run tests

```bash
pytest
```

### 4. Explore the notebook

```bash
jupyter notebook notebooks/exploration.ipynb
```

## Usage: Using the Library

This is a **Python library** for scientific data processing. You can import and use its modules in your own scripts or notebooks.

### Loading and Analyzing Data

```python
import numpy as np
from src.data_loader import load_csv
from src.analysis import calculate_statistics
from src.signal_processing import moving_average, normalize
from src.visualization import plot_signal

# Load experimental data from CSV
df = load_csv('sample_data/experiment_001.csv')
print(df.head())

# Extract the signal column
signal = df['signal'].values

# Calculate descriptive statistics
stats = calculate_statistics(signal)
print(f"Mean: {stats['mean']:.2f}")
print(f"Std Dev: {stats['std']:.2f}")
print(f"Range: [{stats['min']:.2f}, {stats['max']:.2f}]")
```

### Signal Processing

```python
import numpy as np
from src.signal_processing import moving_average, normalize
from src.visualization import plot_signal

# Generate example signal
signal = np.sin(np.linspace(0, 4*np.pi, 200)) + np.random.normal(0, 0.1, 200)

# Apply moving average filter to smooth the signal
smoothed = moving_average(signal, window_size=5)

# Normalize the signal to zero mean and unit variance
normalized = normalize(smoothed)

# Visualize the result
plot_signal(normalized, title="Processed Signal")
```

### In a Jupyter Notebook

Open `notebooks/exploration.ipynb` and run:

```python
from src.data_loader import load_csv
from src.analysis import calculate_statistics

# Load and analyze data
df = load_csv('sample_data/experiment_001.csv')
stats = calculate_statistics(df['signal'].values)
print(stats)
```

## Contributing

For detailed guidelines on the contribution workflow, code standards, versioning strategy, and quality expectations, see [CONTRIBUTING.md](CONTRIBUTING.md).

## Learning Roadmap

See [docs/roadmap.md](docs/roadmap.md) for the complete learning plan.

## Contributing

For detailed guidelines on commits, versioning, and the contribution process, see [CONTRIBUTING.md](CONTRIBUTING.md).

## Architecture

To understand how modules connect, read [docs/architecture.md](docs/architecture.md).

## Main Dependencies

- **pandas** - Data manipulation and analysis
- **numpy** - Numerical computation
- **matplotlib** - Data visualization
- **pytest** - Testing framework
- **jupyter** - Interactive notebooks

## License

MIT
