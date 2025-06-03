"""
Testes para os algoritmos implementados usando as três técnicas de projeto.
"""

import pytest
import sys
import os
import numpy as np

# Adicionar o diretório src ao path do Python
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from dividir_conquistar.merge_sort import merge_sort
from decrementar_conquistar.busca_binaria import busca_binaria
from transformar_conquistar.multiplicacao_matriz import multiplicar_matrizes

def test_merge_sort():
    """Testes para o algoritmo Merge Sort"""
    # Teste com lista vazia
    assert merge_sort([]) == []
    
    # Teste com lista de um elemento
    assert merge_sort([1]) == [1]
    
    # Teste com lista já ordenada
    lista_ordenada = [1, 2, 3, 4, 5]
    assert merge_sort(lista_ordenada) == lista_ordenada
    
    # Teste com lista desordenada
    lista_desordenada = [5, 2, 8, 1, 9]
    assert merge_sort(lista_desordenada) == [1, 2, 5, 8, 9]
    
    # Teste com elementos repetidos
    lista_repetida = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    assert merge_sort(lista_repetida) == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

def test_busca_binaria():
    """Testes para o algoritmo de Busca Binária"""
    lista = [1, 3, 5, 7, 9, 11, 13, 15]
    
    # Teste com elemento presente
    assert busca_binaria(lista, 7) == 3
    
    # Teste com elemento não presente
    assert busca_binaria(lista, 6) == -1
    
    # Teste com primeiro elemento
    assert busca_binaria(lista, 1) == 0
    
    # Teste com último elemento
    assert busca_binaria(lista, 15) == 7
    
    # Teste com lista vazia
    assert busca_binaria([], 5) == -1

def test_multiplicacao_matriz():
    """Testes para o algoritmo de Multiplicação de Matrizes"""
    # Teste com matrizes 2x2
    matriz_a = [[1, 2], [3, 4]]
    matriz_b = [[5, 6], [7, 8]]
    resultado_esperado = np.array([[19, 22], [43, 50]])
    resultado = multiplicar_matrizes(matriz_a, matriz_b)
    assert np.array_equal(resultado, resultado_esperado)
    
    # Teste com matrizes de dimensões diferentes
    matriz_c = [[1, 2, 3], [4, 5, 6]]
    matriz_d = [[7, 8], [9, 10], [11, 12]]
    resultado_esperado_2 = np.array([[58, 64], [139, 154]])
    resultado_2 = multiplicar_matrizes(matriz_c, matriz_d)
    assert np.array_equal(resultado_2, resultado_esperado_2)
    
    # Teste com matrizes incompatíveis
    matriz_incompativel_a = [[1, 2], [3, 4]]
    matriz_incompativel_b = [[1, 2], [3, 4], [5, 6]]  # Agora 2x2 e 3x2, incompatíveis
    try:
        multiplicar_matrizes(matriz_incompativel_a, matriz_incompativel_b)
        assert False, "Deveria ter lançado ValueError"
    except ValueError:
        pass

if __name__ == "__main__":
    pytest.main([__file__]) 