def addLista(listaAdj, de, para, peso):
    listaAdj[de].append((para, peso))
#pior que dijkdtra
def floyd_warshall(V, listaAdj):
    # Inicializa a matriz de distâncias
    dist = [[float('inf')] * V for _ in range(V)]
    for u in range(V):
        dist[u][u] = 0  # Distância de um nó para ele mesmo é 0

    # Preenche as distâncias com base nas arestas
    for u in range(V):
        for v, peso in listaAdj[u]:
            dist[u][v] = min(dist[u][v], peso)

    # Aplica o algoritmo de Floyd-Warshall
    for k in range(V):
        for i in range(V):
            for j in range(V):
                if dist[i][k] < float('inf') and dist[k][j] < float('inf'):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist

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

    # Calcula as distâncias mais curtas entre todos os pares
    dist = floyd_warshall(V, listaAdj)

    # Responde às consultas
    for de, para in consultas:
        if dist[de][para] == float('inf'):
            print("-1")
        else:
            print(dist[de][para])