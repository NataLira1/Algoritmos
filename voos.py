from collections import deque

def addAresta(listaAdj, de, para):
    listaAdj[de].append(para)

def visiteDFS_iterativa(u, listaAdj, visitados):
    stack = [u]  # Pilha para simular a recursão
    while stack:
        atual = stack.pop()
        if not visitados[atual]:
            visitados[atual] = True
            for vizinho in listaAdj[atual]:
                if not visitados[vizinho]:
                    stack.append(vizinho)

def transposta(listaAdj, V):
    transpostaAdj = [[] for _ in range(V)]
    for u in range(V):
        for v in listaAdj[u]:
            transpostaAdj[v].append(u)
    return transpostaAdj

def verificaConexao(listaAdj, V):
    # Verifica se todas as cidades podem ser alcançadas a partir de qualquer cidade
    visitados = [False] * V
    visiteDFS_iterativa(0, listaAdj, visitados)
    if not all(visitados):
        for i in range(V):
            if not visitados[i]:
                return False, 1, i + 1  # Não é possível ir de 1 para i + 1

    # Verifica se todas as cidades podem alcançar a cidade inicial (grafo transposto)
    listaAdjTransposta = transposta(listaAdj, V)
    visitados = [False] * V
    visiteDFS_iterativa(0, listaAdjTransposta, visitados)
    if not all(visitados):
        for i in range(V):
            if not visitados[i]:
                return False, i + 1, 1  # Não é possível ir de i + 1 para 1

    return True, -1, -1

if __name__ == "__main__":
    V, E = map(int, input().split())
    listaAdj = [[] for _ in range(V)]

    for _ in range(E):
        de, para = map(int, input().split())
        addAresta(listaAdj, de - 1, para - 1)

    # Verifica se todas as cidades estão conectadas
    conectado, cidadeA, cidadeB = verificaConexao(listaAdj, V)

    if conectado:
        print("YES")
    else:
        print("NO")
        print(cidadeA, cidadeB)

