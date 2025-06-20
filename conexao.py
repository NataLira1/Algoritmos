import heapq
import sys
sys.setrecursionlimit(10**6)

def inicia(V, origem):
    key = [float('inf')] * V
    key[origem] = 0
    visitados = [False] * V
    return key, visitados 

def prim(listaAdj, origem, V):
    key, visitados = inicia(V, origem)
    heap = [(0, origem)]
    soma_conexao = 0
    cont = 0
    
    while heap:
        custo, u = heapq.heappop(heap)

        if visitados[u]:
            continue
        visitados[u] = True
        soma_conexao += custo
        cont += 1

        for v, peso in listaAdj[u]:
            if not visitados[v] and peso < key[v]:
                key[v] = peso
                heapq.heappush(heap, (key[v], v))
    return soma_conexao if cont == V else "IMPOSSIBLE"

if __name__ == "__main__":
    V, E = map(int, input().split())
    listaAdj = [[] for _ in range(V)]

    for _ in range(E):
        de, para, peso = map(int, input().split())
        listaAdj[de - 1].append((para - 1, peso))
        listaAdj[para - 1].append((de - 1, peso))


    print(prim(listaAdj, 0, V))