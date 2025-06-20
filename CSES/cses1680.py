from collections import deque

def addLista(listaAdj, de, para):
    listaAdj[de].append(para)

if __name__ == "__main__":
    V, E = map(int, input().split())
    listaAdj = [[] for _ in range(V)]
    grausEntrada = [0] * V

    for _ in range(E):
        de, para = map(int, input().split())
        addLista(listaAdj, de - 1, para - 1)
        grausEntrada[para - 1] += 1

    # Ordenação Topológica
    fila = deque()
    for u in range(V):
        if grausEntrada[u] == 0:
            fila.append(u)

    ordenacaoTopologica = []
    while fila:
        u = fila.popleft()
        ordenacaoTopologica.append(u)

        for v in listaAdj[u]:
            grausEntrada[v] -= 1
            if grausEntrada[v] == 0:
                fila.append(v)

    # Inicializa as distâncias e predecessores
    dist = [-float('inf')] * V
    dist[0] = 0  # Distância da cidade 1 para ela mesma é 0
    predecessor = [-1] * V

    # Calcula o caminho mais longo
    for u in ordenacaoTopologica:
        for v in listaAdj[u]:
            if dist[u] + 1 > dist[v]:
                dist[v] = dist[u] + 1
                predecessor[v] = u

    # Verifica se é possível alcançar a cidade n
    if dist[V - 1] == -float('inf'):
        print("IMPOSSIBLE")
    else:
        # Reconstrói o caminho
        caminho = []
        atual = V - 1
        while atual != -1:
            caminho.append(atual + 1)  # Converte para 1-indexado
            atual = predecessor[atual]
        caminho.reverse()

        # Imprime o resultado
        print(len(caminho))
        print(" ".join(map(str, caminho)))