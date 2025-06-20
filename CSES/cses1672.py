import heapq
#dando time limit
def addLista(listaAdj, de, para, peso):
    listaAdj[de].append((para, peso))

def dijkstra(listaAdj, origem, V):
    d = [float('inf')] * V
    d[origem] = 0
    heap = [(0, origem)]

    while heap:
        atualDist, u = heapq.heappop(heap)

        if atualDist > d[u]:
            continue

        for v, peso in listaAdj[u]:
            if d[u] + peso < d[v]:
                d[v] = d[u] + peso
                heapq.heappush(heap, (d[v], v))

    return d

if __name__ == "__main__":
    V, E, C = map(int, input().split())
    listaAdj = [[] for _ in range(V)]

    for _ in range(E):
        de, para, peso = map(int, input().split())
        addLista(listaAdj, de - 1, para - 1, peso)
        addLista(listaAdj, para - 1, de - 1, peso)  # Estradas são bidirecionais

    consultas = []
    for _ in range(C):
        de, para = map(int, input().split())
        consultas.append((de - 1, para - 1))  # Converte para 0-indexado

    # Pré-computa as distâncias de todos os nós para todos os outros
    dist = []
    for u in range(V):
        dist.append(dijkstra(listaAdj, u, V))

    # Responde às consultas
    for de, para in consultas:
        if dist[de][para] == float('inf'):
            print("-1")
        else:
            print(dist[de][para])
