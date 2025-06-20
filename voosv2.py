from collections import deque

# Função para adicionar aresta ao grafo
def addAresta(listaAdj, de, para):
    listaAdj[de].append(para)

# Função DFS para explorar o grafo e marcar os visitados
def DFS(grafo, V, inicio):
    visitado = [False] * V
    pilha = deque([inicio])
    visitado[inicio] = True

    while pilha:
        u = pilha.pop()
        for v in grafo[u]:
            if not visitado[v]:
                visitado[v] = True
                pilha.append(v)

    return visitado

# Função para gerar o grafo transposto
def transposta(listaAdj, V):
    transpostaAdj = [[] for _ in range(V)]
    for u in range(V):
        for v in listaAdj[u]:
            transpostaAdj[v].append(u)
    return transpostaAdj

if __name__ == "__main__":
    # Entrada
    n, m = map(int, input().split())
    listaAdj = [[] for _ in range(n)]
    
    # Leitura das arestas
    for _ in range(m):
        a, b = map(int, input().split())
        addAresta(listaAdj, a - 1, b - 1)  # Ajustando para 0-indexed
    
    # 1. Verificar se todas as cidades são alcançáveis a partir de uma cidade (1-indexada)
    visitado_from_1 = DFS(listaAdj, n, 0)
    
    if not all(visitado_from_1):
        # Se alguma cidade não é alcançável, encontra a primeira cidade não visitada
        for i in range(n):
            if not visitado_from_1[i]:
                print("NÃO")
                print(1, i + 1)  # Exibe cidade 1 (ou qualquer outra) e a cidade desconectada
                break
        exit()
    
    # 2. Grafo transposto
    listaAdjTrans = transposta(listaAdj, n)

    # 3. Verificar se todas as cidades podem acessar a cidade 1 (novamente usando DFS)
    visitado_from_1_trans = DFS(listaAdjTrans, n, 0)

    if not all(visitado_from_1_trans):
        # Se alguma cidade não pode alcançar a cidade 1, então o grafo não é fortemente conexo
        for i in range(n):
            if not visitado_from_1_trans[i]:
                print("NÃO")
                print(i + 1, 1)  # Exibe a cidade que não consegue alcançar a cidade 1
                break
    else:
        print("SIM")
