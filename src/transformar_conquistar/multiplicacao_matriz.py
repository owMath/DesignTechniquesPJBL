"""
Implementação da Multiplicação de Matrizes usando a técnica de Transformar e Conquistar.
Este algoritmo é aplicado no contexto de um sistema de biblioteca para processar
dados de empréstimos e calcular estatísticas.
"""

import numpy as np

def multiplicar_matrizes(matriz_a, matriz_b):
    """
    Implementação da Multiplicação de Matrizes usando a técnica de Transformar e Conquistar.
    
    Args:
        matriz_a: Primeira matriz
        matriz_b: Segunda matriz
        
    Returns:
        Matriz resultante da multiplicação
        
    Raises:
        ValueError: Se as dimensões das matrizes não forem compatíveis para multiplicação
    """
    # Transformar: converter para arrays numpy para melhor performance
    a = np.array(matriz_a)
    b = np.array(matriz_b)
    
    # Verificar se as matrizes podem ser multiplicadas
    if a.shape[1] != b.shape[0]:
        raise ValueError("As dimensões das matrizes não são compatíveis para multiplicação")
    
    # Conquistar: realizar a multiplicação
    return np.dot(a, b)

# Exemplo de uso
if __name__ == "__main__":
    # Exemplo: matriz de empréstimos por mês (3 meses x 4 categorias)
    emprestimos = [
        [10, 15, 8, 12],  # Janeiro
        [12, 18, 9, 14],  # Fevereiro
        [11, 16, 10, 13]  # Março
    ]
    
    # Matriz de pesos para cada categoria
    pesos = [
        [1.2],  # Ficção
        [1.0],  # Não-ficção
        [0.8],  # Referência
        [1.5]   # Periódicos
    ]
    
    print("Matriz de empréstimos:")
    print(np.array(emprestimos))
    print("\nMatriz de pesos:")
    print(np.array(pesos))
    
    resultado = multiplicar_matrizes(emprestimos, pesos)
    print("\nResultado (empréstimos ponderados por mês):")
    print(resultado)

"""
Análise de Eficiência:

1. Complexidade Temporal:
   - Implementação tradicional: O(n³)
   - Implementação com NumPy: O(n².807) usando o algoritmo de Strassen
   - Melhor caso teórico conhecido: O(n².3728596)

2. Complexidade Espacial:
   - O(n²) para armazenar a matriz resultante

3. Vantagens da implementação com NumPy:
   - Código mais limpo e legível
   - Performance otimizada
   - Operações vetorizadas
   - Melhor uso de cache e paralelização

4. Desvantagens:
   - Requer biblioteca externa (NumPy)
   - Overhead de memória para arrays numpy
   - Pode ser menos eficiente para matrizes muito pequenas

5. Comparação com implementação tradicional:
   - Implementação tradicional: O(n³)
   - Implementação NumPy: O(n².807)
   - A implementação NumPy é significativamente mais eficiente para grandes matrizes
""" 