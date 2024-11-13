# test_reto.py

import pytest
from Reto import Reto

def test_Reto_simple():
    n = 4
    weight = [
        [0, 16, 45, 32],
        [16, 0, 18, 21],
        [45, 18, 0, 7],
        [32, 21, 7, 0]
    ]
    mst_edges = Reto(n, weight)
    expected_edges = [(0, 1), (1, 2), (2, 3)]
    assert sorted(mst_edges) == sorted(expected_edges), "El MST no coincide con el esperado."

def test_Reto_disconnected():
    n = 3
    weight = [
        [0, 0, 0],
        [0, 0, 1],
        [0, 1, 0]
    ]
    mst_edges = Reto(n, weight)
    expected_edges = [(1, 2)]
    assert sorted(mst_edges) == sorted(expected_edges), "El MST para grafo desconectado es incorrecto."

def test_Reto_negative_weights():
    n = 3
    weight = [
        [0, -2, 3],
        [-2, 0, 1],
        [3, 1, 0]
    ]
    mst_edges = Reto(n, weight)
    expected_edges = [(0, 1), (1, 2)]
    assert sorted(mst_edges) == sorted(expected_edges), "El MST con pesos negativos es incorrecto."

def test_Reto_zero_weights():
    n = 4
    weight = [
        [0, 0, 0, 1],
        [0, 0, 2, 0],
        [0, 2, 0, 3],
        [1, 0, 3, 0]
    ]
    mst_edges = Reto(n, weight)
    expected_edges = [(0, 3), (3, 2), (2, 1)]
    assert sorted(mst_edges) == sorted(expected_edges), "El MST con pesos cero es incorrecto."

def test_Reto_single_node():
    n = 1
    weight = [
        [0]
    ]
    mst_edges = Reto(n, weight)
    expected_edges = []
    assert mst_edges == expected_edges, "El MST para un solo nodo debe ser vacío."

def test_Reto_large_graph():
    n = 6
    weight = [
        [0, 6, 0, 0, 0, 1],
        [6, 0, 5, 2, 2, 0],
        [0, 5, 0, 5, 0, 0],
        [0, 2, 5, 0, 1, 0],
        [0, 2, 0, 1, 0, 0],
        [1, 0, 0, 0, 0, 0]
    ]
    mst_edges = Reto(n, weight)
    expected_edges = [(0, 5), (5, 1), (1, 3), (3, 4), (1, 2)]
    assert sorted(mst_edges) == sorted(expected_edges), "El MST para el grafo grande es incorrecto."

def test_Reto_invalid_input():
    n = 3
    weight = [
        [0, 1],
        [1, 0, 2],
        [2, 2, 0]
    ]
    with pytest.raises(ValueError, match="La matriz de pesos debe ser de tamaño n x n."):
        Reto(n, weight)
