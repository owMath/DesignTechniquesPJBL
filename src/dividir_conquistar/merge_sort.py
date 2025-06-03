"""
Implementação do Merge Sort usando a técnica de Dividir e Conquistar.
Este algoritmo é aplicado no contexto de um sistema de biblioteca para ordenar
livros por número de identificação.
"""

def merge_sort(lista):
    """
    Implementação do Merge Sort usando a técnica de Dividir e Conquistar.
    
    Args:
        lista: Lista de elementos a serem ordenados
        
    Returns:
        Lista ordenada
    """
    if len(lista) <= 1:
        return lista
    
    # Dividir
    meio = len(lista) // 2
    esquerda = merge_sort(lista[:meio])
    direita = merge_sort(lista[meio:])
    
    # Conquistar
    return merge(esquerda, direita)

def merge(esquerda, direita):
    """
    Função auxiliar para combinar duas listas ordenadas.
    
    Args:
        esquerda: Lista ordenada da esquerda
        direita: Lista ordenada da direita
        
    Returns:
        Lista combinada e ordenada
    """
    resultado = []
    i = j = 0
    
    while i < len(esquerda) and j < len(direita):
        if esquerda[i] <= direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1
    
    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])
    
    return resultado

# Exemplo de uso
if __name__ == "__main__":
    # Exemplo com números de identificação de livros
    livros = [45, 12, 89, 34, 67, 23, 78, 90]
    print("Lista original:", livros)
    livros_ordenados = merge_sort(livros)
    print("Lista ordenada:", livros_ordenados)

"""
Análise de Eficiência:

1. Complexidade Temporal:
   - Melhor caso: O(n log n)
   - Pior caso: O(n log n)
   - Caso médio: O(n log n)

2. Complexidade Espacial:
   - O(n) para armazenar as sublistas temporárias

3. Vantagens:
   - Estável (mantém a ordem relativa de elementos iguais)
   - Performance consistente independente da entrada
   - Bom para grandes conjuntos de dados

4. Desvantagens:
   - Requer espaço adicional para as sublistas
   - Não é in-place
""" 