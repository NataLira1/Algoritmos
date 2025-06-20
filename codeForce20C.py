import heapq

def dijkstra(listaAdj, inicio, fim):
    
    d = [float('inf')] * V
    d[0] = 0
    pred = [-1] * V
    heap = [(0, inicio)]

    while heap:
        atual_dist, u = heapq.heappop(heap)

        if atual_dist > d[u]:
            continue

        for v, peso in listaAdj[u]:
            if d[u] + peso < d[v]:
                d[v] = d[u] + peso
                pred[v] = u
                heapq.heappush(heap, (d[v], v))

    if d[fim] == float('inf'): return -1

    caminho = []
    atual = fim

    while atual != -1:
        caminho.append(atual+1)
        atual = pred[atual]

    return caminho[::-1]

    
V, E = [int(x) for x in input().split(' ')]
listaAdj = [[] for _ in range(V)]

for _ in range(E):
    de, para, peso = [int(x) for x in input().split(' ')]
    listaAdj[de - 1].append((para - 1, peso))
    listaAdj[para - 1].append((de - 1, peso))

caminho = dijkstra(listaAdj,0, V-1)
    
if caminho == -1: print(-1)
else:
    print(" ".join(str(v) for v in caminho))