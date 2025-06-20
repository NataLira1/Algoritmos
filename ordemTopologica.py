from collections import deque

def add_listaAdj(lista, de, para):
    lista[de].append(para)

if __name__ == "__main__":
    V,A = map(int, input().split())
    listaAdj = [[] for _ in range(V)]
    graus_entrada = [0] * V

    #preenchendo lista de adjacentes com arestas
    for _ in range(A):
        de, para = map(int, input().split())
        add_listaAdj(listaAdj, de - 1, para - 1)
        graus_entrada[para - 1] += 1

    fila = deque()
    #ver quais vertices tem grau 0
    for u in range(V):
        if graus_entrada[u] == 0:
            fila.append(u)

    ordenacaoTopologica = []

    while fila:
        u = fila.popleft()
        ordenacaoTopologica.append(u + 1)

        for v in listaAdj[u]:
            graus_entrada[v] -= 1
            if graus_entrada[v] == 0:
                fila.append(v)
    if len(ordenacaoTopologica) != V:
        print("IMPOSSIBLE")
    else:
        print(" ".join(map(str, ordenacaoTopologica)))