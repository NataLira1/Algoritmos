import heapq

def addLista(listaAdj, de, para, peso):
    listaAdj[de].append((para, peso))

def dijkstra(listaAdj,origem, V):
    d = [float('inf')] * V
    pred = [None] * V
    d[origem] = 0
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

    return d

if __name__ == "__main__":
    V, E = map(int, input().split())
    listaAdj = [[] for _ in range(V)]

    for _ in range(E):
        de, para, peso = map(int, input().split())
        addLista(listaAdj, de - 1, para - 1, peso)

    comprimentos = dijkstra(listaAdj, 0, V)
    print(" ".join(str(v) for v in comprimentos))
    