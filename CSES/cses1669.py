import sys
sys.setrecursionlimit(10**6)
#ESTA DANDO TIME LIMIT

def addLista(listaAdj, de, para):
    listaAdj[de].append(para)
    listaAdj[para].append(de)  # Adiciona a aresta na direção oposta (grafo não direcionado)

def encontrarCiclo(listaAdj, V):
    estado = [0] * V  # 0: não visitado, 1: em processamento, 2: processado
    predecessor = [-1] * V
    ciclo = []

    def dfs(u, pai):
        nonlocal ciclo
        estado[u] = 1  # Marca como em processamento
        for v in listaAdj[u]:
            if estado[v] == 0:  # Se o vizinho não foi visitado
                predecessor[v] = u
                if dfs(v, u):
                    return True
            elif estado[v] == 1 and v != pai:  # Encontramos um ciclo (não revisita o pai)
                # Reconstrói o ciclo
                ciclo.append(v)
                atual = u
                while atual != v:
                    ciclo.append(atual)
                    atual = predecessor[atual]
                ciclo.append(v)
                ciclo.reverse()
                return True
        estado[u] = 2  # Marca como processado
        return False

    for u in range(V):
        if estado[u] == 0:
            if dfs(u, -1):  # Passa -1 como pai inicial
                return ciclo

    return None

if __name__ == "__main__":
    V, E = map(int, input().split())
    listaAdj = [[] for _ in range(V)]

    for _ in range(E):
        de, para = map(int, input().split())
        addLista(listaAdj, de - 1, para - 1)

    # Encontra um ciclo no grafo
    ciclo = encontrarCiclo(listaAdj, V)

    if ciclo:
        print(len(ciclo))
        print(" ".join(map(str, [x + 1 for x in ciclo])))  # Converte para 1-indexado
    else:
        print("IMPOSSIBLE")

