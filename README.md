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

## Collaboration Workflow

Follow this workflow to contribute to the project:

### 1. **Create a branch**
```bash
git checkout -b feature/your-feature
# Example: git checkout -b feature/new-analysis
```

### 2. **Implement the feature**
- Write clean code with docstrings and type hints
- Create tests to validate your implementation
- Keep it simple and clear

### 3. **Commit and Push**

We use **Conventional Commits** for clear, structured commit messages:

```bash
git add .
git commit -m "feat(module): add new functionality"
git push origin feature/your-feature
```

**Commit types**:
- `feat:` - A new feature
- `fix:` - A bug fix
- `docs:` - Documentation changes
- `style:` - Code style changes (formatting, missing semicolons, etc)
- `refactor:` - Code refactoring without feature changes
- `perf:` - Performance improvements
- `test:` - Adding or updating tests
- `chore:` - Build, CI, or dependency changes

**Examples**:
```bash
git commit -m "feat(analysis): add moving_average function"
git commit -m "fix(loader): handle missing CSV headers"
git commit -m "docs(roadmap): update week 1 tasks"
git commit -m "test(analysis): add parametrized statistics tests"
```

### 4. **Open a Pull Request**
- Go to the repository on GitHub
- Click "New Pull Request"
- Describe the changes and the reason

### 5. **Code Review**
- Receive feedback from collaborators
- Make adjustments as needed
- Wait for approval

### 6. **Merge**
- After approval, merge to `main`
- Delete the local branch: `git branch -d feature/your-feature`

## Versioning Strategy

We use **Semantic Versioning** (MAJOR.MINOR.PATCH):

- **MAJOR** (x.0.0): Breaking API changes
- **MINOR** (0.x.0): New features (backwards compatible)
- **PATCH** (0.0.x): Bug fixes (backwards compatible)

**Examples**:
- v1.0.0 - Initial release
- v1.1.0 - Added signal filtering feature
- v1.1.1 - Fixed data loader error handling
- v2.0.0 - Complete API redesign

Versions are tagged in Git and automated from conventional commits through CI/CD.

## Quality Standards

- ✨ **Docstrings**: All code must have descriptive docstrings
- 🏷️ **Type Hints**: All parameters and returns must have type hints
- 💬 **Comments**: Only when necessary to clarify complex logic
- ✅ **Tests**: All functionality must have unit tests
- 🎯 **Clarity**: Simple code is better than clever code
- 📝 **Commits**: Follow conventional commits format for clear history
- 🏷️ **Versioning**: Use semantic versioning for releases

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
