# Se nos pide encontrar el cableado más óptimo, por lo que lo ideal sería utilizar un minimum spanning tree, en este caso vamos a usar Prim
# Faltan los typehints, correr el mypy

from typing import List, Tuple, Optional

def Reto(n: int, weight: List[List[int]]) -> List[Tuple[int, int]]:  # "n" es el número de colonias a las que queremos llegar
    if len(weight) != n or any(len(row) != n for row in weight):
        raise ValueError("La matriz de pesos debe ser de tamaño n x n.")
    in_mst: List[bool] = [False] * n
    key: List[float] = [float('inf')] * n  # Es la lista que almacena el peso mínimo de cada vertice 
    parent: List[Optional[int]] = [None] * n

    key[0] = 0

    for _ in range(n):
        u: int = -1
        min_key: float = float('inf')
        for i in range(n):
            if not in_mst[i] and key[i] < min_key:
                min_key = key[i]
                u = i

        if u == -1:
            break  

        in_mst[u] = True

        # Actualizarpara los vértices al lado de u
        for v in range(n):
            if weight[u][v] > 0 and not in_mst[v] and weight[u][v] < key[v]:
                key[v] = weight[u][v]
                parent[v] = u

    #aristas
    mst_edges: List[Tuple[int, int]] = []
    for v in range(1, n):
        p = parent[v]
        if p is not None:
            mst_edges.append((p, v))

    return mst_edges  

# Convertir 0 a 'A', 1 a 'B', etc.
def get_mst_edges_with_colonies(mst_edges: List[Tuple[int, int]]) -> List[str]:
    edge_list: List[str] = []
    for u, v in mst_edges:
        colony_u: str = chr(65 + u)
        colony_v: str = chr(65 + v)
        edge_list.append("({}, {})".format(colony_u, colony_v))
    return edge_list

def main() -> None:
    # Leer datos desd .txt
    try:
        with open('input.txt', 'r') as file:
            lines: List[str] = file.readlines()
    except FileNotFoundError:
        print("El archivo 'input.txt' no se encontró.")
        return

    # Eliminar líneas vacías 
    lines = [line.strip() for line in lines if line.strip() != '']

    if not lines:
        print("El archivo está vacío.")
        return

    # Leer n
    n_line: str = lines.pop(0)
    try:
        n: int = int(n_line)
    except ValueError:
        print("El número de colonias no es válido.")
        return

    if n <= 0:
        print("El número de colonias debe ser un entero positivo.")
        return

    # Leer la matriz de distancias
    weight: List[List[int]] = []
    for i in range(n):
        if not lines:
            print("Faltan datos en la matriz de distancias.")
            return
        row: str = lines.pop(0)
        try:
            weight_row: List[int] = list(map(int, row.strip().split()))
        except ValueError:
            print(f"La fila {i+1} de la matriz contiene valores no enteros.")
            return
        if len(weight_row) != n:
            print(f"La fila {i+1} de la matriz no tiene {n} elementos.")
            return
        weight.append(weight_row)

    mst_edges: List[Tuple[int, int]] = Reto(n, weight)
    edge_list: List[str] = get_mst_edges_with_colonies(mst_edges)
    output: str = ', '.join(edge_list)
    print("Forma óptima de cablear las colonias:")
    print(output)

if __name__ == "__main__":
    main()

# Prueba
# Mover el contenido de la prueba al archivo 'input.txt' y borrar los inputs

# Contenido de 'input.txt':
# 4
# 0 16 45 32
# 16 0 18 21
# 45 18 0 7
# 32 21 7 0
