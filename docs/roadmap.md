# Roadmap de Aprendizagem

## Visão Geral

Estrutura de 6 semanas focada em construir habilidades progressivas em Python, ciência de dados e engenharia de software.

---

## Semana 1: Fundações

### Objetivos
- Dominar Git e workflow colaborativo
- Revisar Python básico
- Aprender manipulação de arquivos CSV

### Tarefas
- [ ] Clonar repositório e configurar ambiente local
- [ ] Revisar branches, commits e Pull Requests
- [ ] Implementar `data_loader.py` para leitura de CSV com pandas
- [ ] Criar testes básicos para carregamento de dados
- [ ] Documentar estrutura de dados no notebook

### Conceitos-chave
- Virtual environments
- Importações Python
- Tipos de dados (listas, dicionários, DataFrames)
- CSV parsing

---

## Semana 2: Testes e Qualidade

### Objetivos
- Aprender pytest
- Escrever testes unitários
- Garantir cobertura de código

### Tarefas
- [ ] Estudar pytest fixtures e assertions
- [ ] Expandir suite de testes
- [ ] Implementar testes parametrizados
- [ ] Configurar relatório de cobertura

### Conceitos-chave
- Unit tests
- Test fixtures
- Mocking
- Cobertura de código

---

## Semana 3: Qualidade de Código

### Objetivos
- Aprender linting e formatação
- Validação de tipos
- Padrões de código

### Tarefas
- [ ] Configurar Ruff para linting
- [ ] Executar Ruff em todo o código
- [ ] Configurar Mypy para type checking
- [ ] Corrigir warnings de tipo
- [ ] Documentar style guide do projeto

### Conceitos-chave
- PEP 8 e PEP 484
- Static type checking
- Code linting
- Pre-commit hooks

---

## Semana 4: Processamento de Sinais

### Objetivos
- Implementar algoritmos de processamento
- Usar NumPy eficientemente
- Validar resultados matemáticos

### Tarefas
- [ ] Implementar `moving_average()` em signal_processing.py
- [ ] Implementar `normalize()` com NumPy
- [ ] Adicionar testes para funções matemáticas
- [ ] Criar visualizações dos resultados

### Conceitos-chave
- Operações NumPy
- Janelas deslizantes (sliding windows)
- Normalização de dados
- Operações vetorizadas

---

## Semana 5: Análise e Visualização

### Objetivos
- Implementar análises estatísticas
- Criar visualizações efetivas
- Interpretar resultados

### Tarefas
- [ ] Implementar `calculate_statistics()` em analysis.py
- [ ] Implementar `plot_signal()` em visualization.py
- [ ] Criar visualizações interativas no notebook
- [ ] Adicionar testes para cálculos estatísticos

### Conceitos-chave
- Estatística descritiva
- Matplotlib e plots
- Interpretação de gráficos
- Boas práticas de visualização

---

## Semana 6: CI/CD e Deployment

### Objetivos
- Configurar integração contínua
- Automatizar testes
- Aprender GitHub Actions

### Tarefas
- [ ] Configurar `.github/workflows/ci.yml`
- [ ] Executar testes automaticamente em PRs
- [ ] Configurar badge de status no README
- [ ] Documentar processo de deploy

### Conceitos-chave
- GitHub Actions
- CI/CD pipelines
- Automatização de testes
- Best practices em deployment

---

## Próximas Etapas (Semana 7+)

### Possíveis extensões
- Integração com instrumentos reais
- Arquitetura em tempo real
- Sistema de cache e persistência
- Logging e monitoramento
- API REST para acesso aos dados
- Containerização com Docker

### Evolução para NICOS
- Este projeto é preparado para evoluir para um sistema similar ao NICOS (Network-based Instrument Control System)
- Estrutura modular permite adicionar controle de instrumentos
- Testes garantem confiabilidade para ambientes experimentais

---

## Recursos Adicionais

### Documentação Recomendada
- [Real Python - Data Science](https://realpython.com)
- [Pandas Documentation](https://pandas.pydata.org)
- [NumPy User Guide](https://numpy.org/doc)
- [Pytest Documentation](https://docs.pytest.org)

### Práticas de Colaboração
- Sempre criar uma branch para novas features
- Abrir PR para revisão antes de merge
- Escrever commits claros e descritivos
- Revisar código dos colegas com construtividade
