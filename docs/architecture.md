# Arquitetura do Sistema

## Fluxo de Dados

```
┌─────────────────┐
│   Data Source   │
│  (CSV, banco)   │
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

## Módulos Principais

### 1. **data_loader.py**

**Responsabilidade**: Carregar e validar dados de fontes externas

**Funções principais**:
- `load_csv(path: str) -> pd.DataFrame` - Carrega arquivo CSV

**Características**:
- Validação básica de formato
- Tratamento de erros
- Type hints completos

**Exemplo**:
```python
from src.data_loader import load_csv

df = load_csv("sample_data/experiment_001.csv")
print(df.head())
```

---

### 2. **signal_processing.py**

**Responsabilidade**: Processar sinais crus, filtrar e transformar dados

**Funções principais**:
- `moving_average(signal: np.ndarray, window_size: int) -> np.ndarray`
- `normalize(signal: np.ndarray) -> np.ndarray`

**Características**:
- Operações vetorizadas com NumPy
- Eficiente para grandes datasets
- Documentação clara de algoritmos

**Exemplo**:
```python
from src.signal_processing import moving_average, normalize

import numpy as np

signal = np.array([1, 2, 3, 4, 5])
smoothed = moving_average(signal, window_size=3)
normalized = normalize(smoothed)
```

---

### 3. **analysis.py**

**Responsabilidade**: Calcular estatísticas e métricas dos dados

**Funções principais**:
- `calculate_statistics(data: np.ndarray) -> dict`

**Retorna**:
- `mean` - Média aritmética
- `std` - Desvio padrão
- `min` - Valor mínimo
- `max` - Valor máximo

**Características**:
- Cálculos estatísticos descritivos
- Retorna dicionário para fácil acesso
- Type hints e docstrings

**Exemplo**:
```python
from src.analysis import calculate_statistics

import numpy as np

data = np.array([1, 2, 3, 4, 5])
stats = calculate_statistics(data)
print(f"Média: {stats['mean']}")
print(f"Desvio padrão: {stats['std']}")
```

---

### 4. **visualization.py**

**Responsabilidade**: Criar gráficos e visualizações dos dados

**Funções principais**:
- `plot_signal(data: np.ndarray, title: str = "Signal") -> None`

**Características**:
- Usa Matplotlib para gráficos
- Configurações sensatas por padrão
- Fácil customização

**Exemplo**:
```python
from src.visualization import plot_signal

import numpy as np

signal = np.sin(np.linspace(0, 2*np.pi, 100))
plot_signal(signal, title="Sine Wave")
```

---

## Fluxo de Uso Típico

### Explorativo (Notebook)
```python
# 1. Carregar dados
df = load_csv("sample_data/experiment_001.csv")

# 2. Processar sinais
signal = df['signal'].values
smoothed = moving_average(signal, window_size=5)

# 3. Analisar
stats = calculate_statistics(smoothed)

# 4. Visualizar
plot_signal(smoothed, title="Processed Signal")
print(stats)
```

### Produtivo (Aplicação)
```python
def process_experiment(csv_path: str) -> dict:
    """Pipeline completo de processamento."""
    # Carregar
    df = load_csv(csv_path)
    signal = df['signal'].values
    
    # Processar
    normalized = normalize(signal)
    smoothed = moving_average(normalized, window_size=3)
    
    # Analisar
    results = calculate_statistics(smoothed)
    
    return results
```

---

## Decisões de Design

### 1. **NumPy vs Pandas**
- Use **NumPy** para processamento de sinais (mais rápido)
- Use **Pandas** para carregamento e manipulação de dados estruturados

### 2. **Type Hints**
- Todos os parâmetros e retornos têm type hints
- Permite detecção de erros com Mypy
- Melhora documentação e autocompletar

### 3. **Docstrings**
- Cada função tem docstring descritiva
- Inclui parâmetros, retorno e exemplos quando relevante
- Formato: Google-style docstrings

### 4. **Modularidade**
- Cada módulo tem responsabilidade clara
- Funções puras (sem side effects quando possível)
- Fácil de testar isoladamente

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
