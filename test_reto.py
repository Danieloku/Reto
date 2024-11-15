# test_Reto.py

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
    expected_edges = [(0, 1), (1, 2), (2, 3)]
    mst_edges = Reto(n, weight)
    assert sorted(mst_edges) == sorted(expected_edges), "El MST no coincide con el esperado."

def test_Reto_un_nodo():
    n = 1
    weight = [
        [0]
    ]
    expected_edges = []
    mst_edges = Reto(n, weight)
    assert mst_edges == expected_edges, "El MST para un solo nodo debe ser vacío."

def test_Reto_grafo_desconectado():
    n = 3
    weight = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    expected_edges = []
    mst_edges = Reto(n, weight)
    assert mst_edges == expected_edges, "El MST para un grafo desconectado debe ser vacío."

def test_Reto_entrada_invalida():
    n = 3
    weight = [
        [0, 1],
        [1, 0, 2],
        [2, 2, 0]
    ]
    with pytest.raises(ValueError):
        Reto(n, weight)
