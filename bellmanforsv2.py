def addLista(listaAdj, de, para, peso):
    listaAdj[de].append((para, peso))

def inicia(V, origem):
    d = [float('inf')] * V       # Inicializa distâncias com infinito
    pred = [None] * V            # Inicializa predecessores como None
    d[origem] = 0                # A distância da origem para ela mesma é 0
    return d, pred

def relaxa( u, v, d, pred, peso):
    if d[v] > d[u] + peso:
        d[v] = d[u] + peso
        pred[v] = u

def bellmanFord(listaAdj, arestas ,origem, V):
    d, pred = inicia(V, origem)

    for _ in range(V - 1):
        for u, v, peso in arestas:
            relaxa(u, v, d, pred, peso)

    # Verifica ciclo negativo
    for u, v, peso in arestas:
        if d[v] > d[u] + peso:
            print("Ciclo de peso negativo detectado!")
            return None, None

    return d, pred


if __name__ == "__main__":
    
    V, E = map(int, input().split())
    listaAdj = [[] for _ in range(V)]

    arestas = []

    for _ in range(E):
        de, para, peso = map(int, input().split())
        addLista(listaAdj, de - 1, para - 1, peso)
        arestas.append((de - 1, para - 1, peso))

    origem = int(input("Origem: ")) - 1
    d, pred = bellmanFord(listaAdj, arestas ,origem, V)

    print("Distâncias:", d)
    print("Predecessores:", pred)