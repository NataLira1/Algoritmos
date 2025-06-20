import heapq
from collections import defaultdict

def addLista(listaAdj, de, para, peso):
    listaAdj[de].append((para, peso))

def kRotasMaisBaratas(listaAdj, V, k):
    # Armazena as k menores distâncias para cada cidade
    distancias = defaultdict(list)
    distancias[0].append(0)  # Começamos na cidade 1 (índice 0) com custo 0
    heap = [(0, 0)]  # (custo atual, cidade atual)
    resultados = []
    while heap:
        custoAtual, u = heapq.heappop(heap)

        # Se já temos k distâncias para a cidade `n`, ignoramos rotas mais caras
        if u == V - 1:
            resultados.append(custoAtual)
            if len(resultados) == k:
                return resultados

        for v, peso in listaAdj[u]:
            novoCusto = custoAtual + peso

            # Se ainda não temos k distâncias para `v`, adicionamos
            if len(distancias[v]) < k:
                heapq.heappush(heap, (novoCusto, v))
                heapq.heappush(distancias[v], -novoCusto)  # Usamos -custo para simular um max-heap
            # Se já temos k distâncias, substituímos a maior se o novo custo for menor
            elif -distancias[v][0] > novoCusto:
                heapq.heappop(distancias[v])
                heapq.heappush(distancias[v], -novoCusto)
                heapq.heappush(heap, (novoCusto, v))
    return resultados

if __name__ == "__main__":
    
    V, E, k = map(int, input().split())
    listaAdj = [[] for _ in range(V)]

    for _ in range(E):
        de, para, peso = map(int, input().split())
        addLista(listaAdj, de - 1, para - 1, peso)

    resultado = kRotasMaisBaratas(listaAdj, V, k)
    print(" ".join(map(str, resultado)))