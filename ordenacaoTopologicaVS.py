from collections import deque

def addVertice(lista, de, para):
    lista[de].append(para)

if __name__ == "__main__":
    V, E = map(int, input().split())
    list_adj = [[] for _ in range(V)]
    in_degree = [0] * V

    for _ in range(E):
        de, para = map(int, input().split())
        addVertice(list_adj, de - 1, para - 1)
        in_degree[para - 1] += 1

    # Fila com vértices de grau de entrada 0
    fila = deque()
    for i in range(V):
        if in_degree[i] == 0:
            fila.append(i)

    ordem_topologica = []

    while fila:
        u = fila.popleft()
        ordem_topologica.append(u + 1)  # ajusta para 1-based

        for v in list_adj[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                fila.append(v)

    # Se não adicionamos todos os vértices, há um ciclo
    if len(ordem_topologica) != V:
        print("IMPOSSIBLE")
    else:
        print(" ".join(map(str, ordem_topologica)))
