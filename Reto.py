#Se nos pide encontrear el cableado + optimo por lo que lo ideal sería utilizar un minimum spanning tree, en este caso vamos a usar Prim

def Reto(n, weight): # "n" es el numero de colonias a las que queremos llegar
    in_mst = [False] * n
    key = [float('inf')] * n #es la lista que almacena el peso mínimo para llegar a cada vértice desde el MST
    parent = [None] * n

    key[0] = 0

    for _ in range(n):
        u = -1
        min_key = float('inf')
        for i in range(n):
            if not in_mst[i] and key[i] < min_key:
                min_key = key[i]
                u = i

        in_mst[u] = True

        # Actualizar key y parent para los vértices adyacentes a u
        for v in range(n):
            if weight[u][v] > 0 and not in_mst[v] and weight[u][v] < key[v]:
                key[v] = weight[u][v]
                parent[v] = u

    # Recopilar las aristas en el MST
    mst_edges = []
    for v in range(1, n):
        if parent[v] is not None:
            mst_edges.append((parent[v], v))

    return mst_edges

# Convertir 0 a 'A', 1 a 'B', etc.
def get_mst_edges_with_colonies(mst_edges):
    
    edge_list = []
    for u, v in mst_edges:
        colony_u = chr(65 + u)  
        colony_v = chr(65 + v)
        edge_list.append("({}, {})".format(colony_u, colony_v))
    return edge_list

def main():
    n = int(input("Ingresa el número de colonias: "))
    print("Ingresa la matriz de distancias ({} filas de {} números):".format(n, n))
    weight = []
    for _ in range(n):
        while True:
            row = input()
            if row.strip() == '':
                continue  # Ignorar líneas vacías
            row = list(map(int, row.strip().split()))
            if len(row) != n:
                print("Debe ingresar exactamente {} números por fila.".format(n))
                continue
            weight.append(row)
            break

    mst_edges = Reto(n, weight)
    edge_list = get_mst_edges_with_colonies(mst_edges)
    output = ', '.join(edge_list)
    print("Forma óptima de cablear las colonias:")
    print(output)

if __name__ == "__main__":
    main()

        #Prueba
    #4
    #0 16 35 32
    #16 0 18 21
    #45 18 0 7
    #32 21 7 0