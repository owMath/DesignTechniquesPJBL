"""
Implementação da Busca Binária usando a técnica de Decrementar e Conquistar.
Este algoritmo é aplicado no contexto de um sistema de biblioteca para buscar
livros por número de identificação em uma lista ordenada.
"""

def busca_binaria(lista, elemento):
    """
    Implementação da Busca Binária usando a técnica de Decrementar e Conquistar.
    
    Args:
        lista: Lista ordenada de elementos
        elemento: Elemento a ser encontrado
        
    Returns:
        Índice do elemento se encontrado, -1 caso contrário
    """
    esquerda = 0
    direita = len(lista) - 1
    
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        
        # Caso base: elemento encontrado
        if lista[meio] == elemento:
            return meio
        
        # Decrementar: reduzir o espaço de busca pela metade
        if lista[meio] < elemento:
            esquerda = meio + 1
        else:
            direita = meio - 1
    
    return -1

# Exemplo de uso
if __name__ == "__main__":
    # Exemplo com números de identificação de livros ordenados
    livros = [12, 23, 34, 45, 67, 78, 89, 90]
    livro_procurado = 45
    
    print("Lista de livros:", livros)
    print(f"Procurando livro com ID {livro_procurado}")
    
    indice = busca_binaria(livros, livro_procurado)
    if indice != -1:
        print(f"Livro encontrado na posição {indice}")
    else:
        print("Livro não encontrado")

"""
Análise de Eficiência:

1. Complexidade Temporal:
   - Melhor caso: O(1) - elemento encontrado no meio
   - Pior caso: O(log n) - elemento não encontrado
   - Caso médio: O(log n)

2. Complexidade Espacial:
   - O(1) - usa apenas variáveis auxiliares

3. Vantagens:
   - Extremamente eficiente para listas ordenadas
   - Complexidade logarítmica
   - Não requer espaço adicional significativo

4. Desvantagens:
   - Requer que a lista esteja ordenada
   - Não é eficiente para listas pequenas
   - Não funciona bem com listas que mudam frequentemente

5. Comparação com Busca Linear:
   - Busca Linear: O(n)
   - Busca Binária: O(log n)
   - A busca binária é significativamente mais eficiente para grandes conjuntos de dados
""" 