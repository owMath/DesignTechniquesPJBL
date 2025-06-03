# Análise de Técnicas de Projeto de Algoritmos

## GRUPO 4
Giovanna Caroline Zettel Francisco

Leonardo Augusto Dolvitsch

Matheus Paul Lopuch


### Este projeto demonstra a implementação e análise de três diferentes técnicas de projeto de algoritmos aplicadas a um sistema de gerenciamento de biblioteca.

Problema 1: Dividir e Conquistar

Problema 2: Decrementar e Conquistar

Problema 3: Transformar e Conquistar

## 🚀 Como Executar

### Pré-requisitos
- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

### Instalação

1. Instale as dependências:
```bash
pip install -r requirements.txt
```

### Executando os Algoritmos

Para executar cada algoritmo individualmente:

1. **Merge Sort (Dividir e Conquistar)**:
```bash
python src/dividir_conquistar/merge_sort.py
```

2. **Busca Binária (Decrementar e Conquistar)**:
```bash
python src/decrementar_conquistar/busca_binaria.py
```

3. **Multiplicação de Matrizes (Transformar e Conquistar)**:
```bash
python src/transformar_conquistar/multiplicacao_matriz.py
```

### Executando os Testes

Para executar todos os testes automatizados:
```bash
pytest tests/test_algoritmos.py -v
```

Para executar um teste específico:
```bash
pytest tests/test_algoritmos.py::test_merge_sort -v
pytest tests/test_algoritmos.py::test_busca_binaria -v
pytest tests/test_algoritmos.py::test_multiplicacao_matriz -v
```

## 📊 Análise de Eficiência

Cada algoritmo inclui uma análise detalhada de sua complexidade temporal e espacial:

1. **Merge Sort**:
   - Complexidade Temporal: O(n log n)
   - Complexidade Espacial: O(n)

2. **Busca Binária**:
   - Complexidade Temporal: O(log n)
   - Complexidade Espacial: O(1)

3. **Multiplicação de Matrizes**:
   - Complexidade Temporal: O(n².807)
   - Complexidade Espacial: O(n²)
