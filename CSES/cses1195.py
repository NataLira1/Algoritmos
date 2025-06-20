import heapq
import math
#Esta dando time lim
def addLista(listaAdj, de, para, peso):
    listaAdj[de].append((para, peso))

def dijkstraComDesconto(listaAdj, V):
    # d[u][0]: Menor custo para chegar a `u` sem usar o cupom
    # d[u][1]: Menor custo para chegar a `u` após usar o cupom
    d = [[float('inf')] * 2 for _ in range(V)]
    d[0][0] = 0  # Começamos na cidade 1 (índice 0) sem usar o cupom
    heap = [(0, 0, 0)]  # (custo atual, cidade atual, cupom usado: 0 ou 1)
    while heap:
        custoAtual, u, usadoCupom = heapq.heappop(heap)
        # Ignora estados que já foram processados com menor custo
        if custoAtual > d[u][usadoCupom]:
            continue
        for v, peso in listaAdj[u]:
            # Caso 1: Usar o voo normalmente
            if d[v][usadoCupom] > custoAtual + peso:
                d[v][usadoCupom] = custoAtual + peso
                heapq.heappush(heap, (d[v][usadoCupom], v, usadoCupom))
            # Caso 2: Usar o cupom (se ainda não foi usado)
            if usadoCupom == 0:
                custoComDesconto = custoAtual + math.floor(peso / 2)
                if d[v][1] > custoComDesconto:
                    d[v][1] = custoComDesconto
                    heapq.heappush(heap, (d[v][1], v, 1))
    # Retorna o menor custo para chegar à cidade `n` (índice V-1)
    return min(d[V-1][0], d[V-1][1])

if __name__ == "__main__":
    V, E = map(int, input().split())
    listaAdj = [[] for _ in range(V)]

    for _ in range(E):
        de, para, peso = map(int, input().split())
        addLista(listaAdj, de - 1, para - 1, peso)

    resultado = dijkstraComDesconto(listaAdj, V)
    print(resultado)