import heapq

def addVertice(listaAdj, de, para, peso):
    listaAdj[de].append((para, peso))
    listaAdj[para].append((para, peso))

def inicia(V, origem):
    pred = [None] * V
    d = [float('inf')] * V
    d[origem] = 0
    return pred, d

def dijkstra(listaAdj, origem, V):
    pred, d = inicia(V, origem)
    heap = [(0, origem)]

    while heap:
        atual_dist, u = heapq.heappop(heap)

        if atual_dist > d[u]:
            continue

        for v, peso in listaAdj[u]:
            if d[u] + peso < d[v]:
                d[v] = d[u] + peso
                pred[v] = u
                heapq.heappush(heap, (d[v], v))

    return pred

def reconstrui_caminho(pred, inicio, fim):
    caminho = []
    atual = fim

    while atual is not None:
        caminho.append(atual)
        atual = pred[atual]

    caminho.reverse()

    if caminho[0] == inicio:
        return caminho
    else:
        return -1  # Não existe caminho


if __name__ == "__main__":
    V, E = map(int, input().split())
    listaAdj = [[] for _ in range(V)]

    for _ in range(E):
        de, para, peso = map(int, input().split())
        addVertice(listaAdj, de - 1, para - 1, peso)
    
    origem = 0            # vértice 1 no input (índice 0)
    destino = V - 1       # vértice n no input (índice V - 1)

    pred = dijkstra(listaAdj, origem, V)
    caminho = reconstrui_caminho(pred, origem, destino)

    if caminho == -1:
        print(-1)
    else:
        print(' '.join(str(v + 1) for v in caminho))


