import heapq

def addLista(lista, de, para, peso):
    lista[de].append((para, peso))
    lista[para].append((de, peso))

def inicia(V, origem):
    key = [float('inf')] * V
    pi = [None] * V
    key[origem] = 0
    return key, pi 

def prim(listaAdj, origem, V):
    key, pi = inicia(V, origem)
    heap = [(0, origem)]
    visitados = set()
    
    while heap:
        _, u = heapq.heappop(heap)

        if u in visitados:
            continue
        visitados.add(u)

        for v, peso in listaAdj[u]:
            if v not in visitados and peso < key[v]:
                key[v] = peso
                pi[v] = u
                heapq.heappush(heap, (key[v], v))
    return key, pi

if __name__ == "__main__":
    V, E = map(int, input().split())
    listaAdj = [[] for _ in range(V)]

    for _ in range(E):
        de, para, peso = map(int, input().split())
        addLista(listaAdj, de - 1, para - 1, peso)


    origem = int(input("Origem: ")) - 1

    chave, pred = prim(listaAdj, origem, V)

    print(chave)
    print(pred)