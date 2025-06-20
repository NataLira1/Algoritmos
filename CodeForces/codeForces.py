import heapq

def inicia(V, origem):
    dist = [float('inf')] * V
    dist[origem] = 0
    return dist

def addLista(listaAdj, de, para, peso):
    listaAdj[de].append((para, peso))
    listaAdj[para].append((de, peso))
    
def dijkstra(listaAdj, origem , V, semaforos):
    dist= inicia(V, origem)
    heap = [(0, origem)]

    while heap:
        tempo_atual, u = heapq.heappop(heap)

        if tempo_atual > dist[u]:
            continue
        
        while tempo_atual in semaforos[u]:
            tempo_atual += 1

        for v, peso in listaAdj[u]:
            chegada = tempo_atual + peso

            if chegada < dist[v]:
                dist[v] = chegada
                heapq.heappush(heap, (chegada, v))
        
    return -1 if dist[V-1] == float('inf') else dist[V-1]

if __name__ == "__main__":
    V, E = map(int, input().split())
    listaAdj = [[] for _ in range(V)]

    for _ in range(E):
        de, para, peso = map(int, input().split())
        addLista(listaAdj, de - 1, para - 1, peso)

    semaforos = []
    for _ in range(V):
        dados = list(map(int, input().split()))
        semaforos.append(set(dados[1:dados[0] + 1]))

    print(dijkstra(listaAdj, 0, V, semaforos))