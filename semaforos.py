import heapq

def inicia(V, origem): 
    pred = [None] * V
    d = [float('inf')] * V
    d[origem] = 0
    return pred, d

def addLista(listaAdj, de, para, peso):
    listaAdj[de].append((para, peso))

def dijkstra(listaAdj, origem, V, semaforos):
    pred, d = inicia(V, origem)
    heap = [(0, origem)]

    while heap:
        atual_dist, u = heapq.heappop(heap)

        if atual_dist > d[u]:
            continue

        for v, peso in listaAdj[u]:
            chegada = atual_dist + peso

            while chegada in semaforos[v]:
                chegada += 1

            if chegada < d[v]:
                d[v] = chegada
                pred[v] = u
                heapq.heappush(heap, (d[v], v))
    cont = 0
    for pi in pred:
        if pi == None:
            cont += 1
    if cont != 1:
        return -1
    else:
        return d[-1]

if __name__ == "__main__":
    V, E = map(int, input().split())
    listaAdj = [[] for _ in range(V)]
    for _ in range(E):
        de, para, peso = map(int, input().split())
        addLista(listaAdj, de - 1, para - 1, peso)

    semaforos = []
    for _ in range(V):
        linha = list(map(int, input().split()))
        k = linha[0]
        semaforos.append(linha[1:k+1])

    print(dijkstra(listaAdj, 0, V, semaforos))

   