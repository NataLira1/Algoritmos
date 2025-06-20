import heapq

def inicia(V, origem): 
    pred = [None] * V
    d = [float('inf')] * V
    d[origem] = 0
    return pred, d

def addLista(listaAdj, de, para, peso):
    listaAdj[de].append((para, peso))

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

    return d, pred

if __name__ == "__main__":

    V, E = map(int, input().split())
    listaAdj = [[] for _ in range(V)]
    for _ in range(E):
        de, para, peso = map(int, input().split())
        addLista(listaAdj, de - 1, para - 1, peso)

    origem = int(input("Origem: ")) - 1
    distancias, predecessor = dijkstra(listaAdj, origem, V)

    print(distancias)
    print(predecessor)
    