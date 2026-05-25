# System Architecture

## Data Flow

```
┌─────────────────┐
│   Data Source   │
│  (CSV, Database)│
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Data Loader    │
│   (load_csv)    │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Signal Process. │
│  (filters, etc) │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│    Analysis     │
│  (statistics)   │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Visualization   │
│    (plots)      │
└─────────────────┘
```

## Main Modules

### 1. **data_loader.py**

**Responsibility**: Load and validate data from external sources

**Main functions**:
- `load_csv(path: str) -> pd.DataFrame` - Loads CSV file

**Features**:
- Basic format validation
- Error handling
- Complete type hints

**Example**:
```python
from src.data_loader import load_csv

df = load_csv("sample_data/experiment_001.csv")
print(df.head())
```

---

### 2. **signal_processing.py**

**Responsibility**: Process raw signals, filter and transform data

**Main functions**:
- `moving_average(signal: np.ndarray, window_size: int) -> np.ndarray`
- `normalize(signal: np.ndarray) -> np.ndarray`

**Features**:
- Vectorized operations with NumPy
- Efficient for large datasets
- Clear algorithm documentation

**Example**:
```python
from src.signal_processing import moving_average, normalize

import numpy as np

signal = np.array([1, 2, 3, 4, 5])
smoothed = moving_average(signal, window_size=3)
normalized = normalize(smoothed)
```

---

### 3. **analysis.py**

**Responsibility**: Calculate statistics and metrics of the data

**Main functions**:
- `calculate_statistics(data: np.ndarray) -> dict`

**Returns**:
- `mean` - Arithmetic mean
- `std` - Standard deviation
- `min` - Minimum value
- `max` - Maximum value

**Features**:
- Descriptive statistical calculations
- Returns dictionary for easy access
- Type hints and docstrings

**Example**:
```python
from src.analysis import calculate_statistics

import numpy as np

data = np.array([1, 2, 3, 4, 5])
stats = calculate_statistics(data)
print(f"Mean: {stats['mean']}")
print(f"Standard deviation: {stats['std']}")
```

---

### 4. **visualization.py**

**Responsibility**: Create graphs and data visualizations

**Main functions**:
- `plot_signal(data: np.ndarray, title: str = "Signal") -> None`

**Features**:
- Uses Matplotlib for graphs
- Sensible defaults
- Easy customization

**Example**:
```python
from src.visualization import plot_signal

import numpy as np

signal = np.sin(np.linspace(0, 2*np.pi, 100))
plot_signal(signal, title="Sine Wave")
```

---

## Typical Usage Flow

### Exploratory (Notebook)
```python
# 1. Load data
df = load_csv("sample_data/experiment_001.csv")

# 2. Process signals
signal = df['signal'].values
smoothed = moving_average(signal, window_size=5)

# 3. Analyze
stats = calculate_statistics(smoothed)

# 4. Visualize
plot_signal(smoothed, title="Processed Signal")
print(stats)
```

### Production (Application)
```python
def process_experiment(csv_path: str) -> dict:
    """Complete processing pipeline."""
    # Load
    df = load_csv(csv_path)
    signal = df['signal'].values
    
    # Process
    normalized = normalize(signal)
    smoothed = moving_average(normalized, window_size=3)
    
    # Analyze
    results = calculate_statistics(smoothed)
    
    return results
```

---

## Design Decisions

### 1. **NumPy vs Pandas**
- Use **NumPy** for signal processing (faster)
- Use **Pandas** for loading and manipulating structured data

### 2. **Type Hints**
- All parameters and returns have type hints
- Allows error detection with Mypy
- Improves documentation and autocomplete

### 3. **Docstrings**
- Each function has a descriptive docstring
- Includes parameters, return value, and examples when relevant
- Format: Google-style docstrings

### 4. **Modularity**
- Each module has clear responsibility
- Pure functions (no side effects when possible)
- Easy to test in isolation

---

## Expansão Futura

### Preparação para NICOS-like
```
┌─────────────────────────────────────┐
│   Instrument Control Layer          │
│  (Communication, Hardware Control)  │
└─────────────────┬───────────────────┘
                  │
┌─────────────────▼───────────────────┐
│   Current Architecture              │
│  (Data Processing Pipeline)         │
└─────────────────────────────────────┘
```

### Possíveis Adições
- **Logging**: Sistema de logging centralizado
- **Caching**: Persistência de resultados intermediários
- **API**: REST API para acesso aos dados
- **Real-time**: Processamento em tempo real de streams
- **Database**: Armazenamento de histórico experimental

---

## Padrões de Contribuição

Ao adicionar novos módulos:

1. **Mantenha a simplicidade** - Não adicione abstrações prematuras
2. **Documente claramente** - Docstrings explicativas
3. **Teste thoroughly** - Cobertura mínima 80%
4. **Siga os padrões** - Type hints, PEP 8, etc
5. **Integre no pipeline** - Atualize fluxos quando necessário
