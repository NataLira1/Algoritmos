import sys
input = sys.stdin.read
#dadno time limit
def addLista(listaAdj, de, para, peso):
    listaAdj[de].append((para, peso))

def inicia(V, origem):
    d = [-float('inf')] * V  # Inicializa distâncias com -infinito (para maximizar)
    d[origem] = 0            # A distância da origem para ela mesma é 0
    return d

def relaxa(u, v, d, peso):
    if d[u] != -float('inf') and d[v] < d[u] + peso:
        d[v] = d[u] + peso
        return True
    return False

def bellmanFord(listaAdj, origem, V):
    d = inicia(V, origem)
    # Relaxa as arestas V-1 vezes
    for _ in range(V - 1):
        for u in range(V):
            for v, peso in listaAdj[u]:
                relaxa(u, v, d, peso)
    # Detecta ciclos positivos
    for _ in range(V):  # Relaxa mais uma vez para verificar ciclos
        for u in range(V):
            for v, peso in listaAdj[u]:
                if relaxa(u, v, d, peso):
                    # Se o nó `v` puder ser atualizado, há um ciclo positivo
                    if podeAlcancar(listaAdj, v, V - 1):
                        return -1  # Pontuação arbitrariamente grande
    return d[V - 1]  # Retorna a pontuação máxima para o último nó

def podeAlcancar(listaAdj, origem, destino):
    # Verifica se é possível alcançar o destino a partir da origem
    visitado = [False] * len(listaAdj)
    stack = [origem]
    while stack:
        u = stack.pop()
        if u == destino:
            return True
        if not visitado[u]:
            visitado[u] = True
            for v, _ in listaAdj[u]:
                stack.append(v)
    return False

if __name__ == "__main__":
    # Lê toda a entrada de uma vez
    dados = input().split()
    # Lê o número de vértices e arestas
    V, E = int(dados[0]), int(dados[1])
    listaAdj = [[] for _ in range(V)]
    # Lê as arestas
    index = 2
    for _ in range(E):
        de, para, peso = int(dados[index]), int(dados[index + 1]), int(dados[index + 2])
        addLista(listaAdj, de - 1, para - 1, peso)
        index += 3
    # Executa o algoritmo de Bellman-Ford
    resultado = bellmanFord(listaAdj, 0, V)
    if resultado == -1:
        print("-1")
    else:
        print(resultado)