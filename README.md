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

### 3. Run tests

```bash
pytest
```

### 4. Explore the notebook

```bash
jupyter notebook notebooks/exploration.ipynb
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
```bash
git add .
git commit -m "Add new functionality"
git push origin feature/your-feature
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

## Quality Standards

- ✨ **Docstrings**: All code must have descriptive docstrings
- 🏷️ **Type Hints**: All parameters and returns must have type hints
- 💬 **Comments**: Only when necessary to clarify complex logic
- ✅ **Tests**: All functionality must have unit tests
- 🎯 **Clarity**: Simple code is better than clever code

## Learning Roadmap

See [docs/roadmap.md](docs/roadmap.md) for the complete learning plan.

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
