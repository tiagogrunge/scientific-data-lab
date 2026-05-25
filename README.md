# Scientific Data Lab

## Propósito

O **Scientific Data Lab** é um projeto de aprendizagem colaborativa focado em:

- 🐍 **Python aplicado a dados científicos** - Aprenda a processar, analisar e visualizar dados experimentais
- 🔗 **Git e colaboração** - Pratique Git, Pull Requests e revisão de código em um ambiente educacional
- ✅ **Qualidade de software** - Aprenda sobre testes unitários, CI/CD, type hints e linting
- 🧪 **Boas práticas de engenharia** - Estrutura preparada para evoluir futuramente para sistemas de instrumentação científica como NICOS

## Estrutura do Projeto

```
scientific-data-lab/
├── README.md                 # Este arquivo
├── docs/                     # Documentação
│   ├── roadmap.md           # Plano de aprendizagem
│   ├── architecture.md       # Arquitetura do sistema
│   └── learning-notes/       # Notas de aprendizagem
├── src/                      # Código-fonte principal
│   ├── __init__.py
│   ├── data_loader.py        # Carregamento de dados
│   ├── signal_processing.py  # Processamento de sinais
│   ├── analysis.py           # Análise estatística
│   └── visualization.py      # Visualização de dados
├── tests/                    # Testes unitários
│   ├── __init__.py
│   ├── test_loader.py
│   └── test_analysis.py
├── sample_data/              # Dados de exemplo
│   └── experiment_001.csv
├── notebooks/                # Jupyter notebooks
│   └── exploration.ipynb
├── .github/                  # Configuração GitHub
│   └── workflows/
│       └── ci.yml            # Pipeline CI/CD
├── requirements.txt          # Dependências Python
├── .gitignore                # Arquivos a ignorar no Git
└── pyproject.toml            # Configuração de ferramentas
```

## Quick Start

### 1. Configurar ambiente virtual

```bash
# Criar virtual environment
python -m venv .venv

# Ativar (Linux/macOS)
source .venv/bin/activate

# Ativar (Windows)
.venv\Scripts\activate
```

### 2. Instalar dependências

```bash
pip install -r requirements.txt
```

### 3. Executar testes

```bash
pytest
```

### 4. Explorar o notebook

```bash
jupyter notebook notebooks/exploration.ipynb
```

## Fluxo de Colaboração

Siga este fluxo para contribuir com o projeto:

### 1. **Criar uma branch**
```bash
git checkout -b feature/sua-feature
# Exemplo: git checkout -b feature/nova-analise
```

### 2. **Implementar a feature**
- Escreva código limpo com docstrings e type hints
- Crie testes para validar sua implementação
- Mantenha a simplicidade e clareza

### 3. **Commit e Push**
```bash
git add .
git commit -m "Adiciona nova funcionalidade"
git push origin feature/sua-feature
```

### 4. **Abrir Pull Request**
- Vá para o repositório no GitHub
- Clique em "New Pull Request"
- Descreva as mudanças e o motivo

### 5. **Revisão de Código**
- Receba feedback dos colaboradores
- Faça ajustes conforme necessário
- Aguarde aprovação

### 6. **Merge**
- Após aprovação, faça merge para `main`
- Delete a branch local: `git branch -d feature/sua-feature`

## Padrões de Qualidade

- ✨ **Docstrings**: Todo código deve ter docstrings descritivas
- 🏷️ **Type Hints**: Todos os parâmetros e retornos devem ter type hints
- 💬 **Comentários**: Apenas quando necessários para esclarecer lógica complexa
- ✅ **Testes**: Toda funcionalidade deve ter testes unitários
- 🎯 **Clareza**: Código simples é melhor que código inteligente

## Roadmap de Aprendizagem

Consulte [docs/roadmap.md](docs/roadmap.md) para o plano completo de aprendizagem.

## Arquitetura

Para entender como os módulos se conectam, leia [docs/architecture.md](docs/architecture.md).

## Dependências Principais

- **pandas** - Manipulação e análise de dados
- **numpy** - Computação numérica
- **matplotlib** - Visualização de dados
- **pytest** - Framework de testes
- **jupyter** - Notebooks interativos

## Licença

MIT
