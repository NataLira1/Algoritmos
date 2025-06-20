import heapq

def dijkstra(n, grafo, semaforos):
    # Tempo inicial, considerando se o semáforo inicial está fechado
    tempo_inicial = 0
    while tempo_inicial in semaforos[0]:
        tempo_inicial += 1

    # Inicializa a distância para todos os semáforos
    dist = [float('inf')] * n
    dist[0] = tempo_inicial

    # Heap de prioridade (tempo, nó atual)
    heap = [(tempo_inicial, 0)]

    while heap:
        tempo_atual, u = heapq.heappop(heap)

        if tempo_atual > dist[u]:
            continue

        for v, custo in grafo[u]:
            chegada = tempo_atual + custo

            # Esperar se o semáforo estiver fechado
            while chegada in semaforos[v]:
                chegada += 1

            if chegada < dist[v]:
                dist[v] = chegada
                heapq.heappush(heap, (chegada, v))

    return -1 if dist[n-1] == float('inf') else dist[n-1]

# Função principal para leitura e execução
def main():
    n, m = map(int, input().split())
    grafo = [[] for _ in range(n)]

    for _ in range(m):
        u, v, w = map(int, input().split())
        grafo[u-1].append((v-1, w))
        grafo[v-1].append((u-1, w))  # Grafo não direcionado

    semaforos = []
    for _ in range(n):
        dados = list(map(int, input().split()))
        fechados = set(dados[1:]) if dados[0] > 0 else set()
        semaforos.append(fechados)

    print(dijkstra(n, grafo, semaforos))

if __name__ == "__main__":
    main()
