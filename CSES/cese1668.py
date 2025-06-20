import sys
sys.setrecursionlimit(10**6)

def addLista(listaAdj, de, para):
    listaAdj[de].append(para)
    listaAdj[para].append(de)  # Adiciona a aresta na direção oposta (grafo não direcionado)

def bipartirGrafoDFS(listaAdj, V):
    equipes = [0] * V  # 0: não visitado, 1: equipe 1, 2: equipe 2
    def dfs(u, equipe):
        equipes[u] = equipe
        for v in listaAdj[u]:
            if equipes[v] == 0:  # Se o nó ainda não foi visitado
                if not dfs(v, 3 - equipe):  # Alterna entre 1 e 2
                    return False
            elif equipes[v] == equipe:  # Conflito encontrado
                return False
        return True
    # Verifica cada componente conexo
    for u in range(V):
        if equipes[u] == 0:  # Se o nó ainda não foi visitado
            if not dfs(u, 1):  # Começa atribuindo à equipe 1
                return "IMPOSSIBLE"

    return equipes

if __name__ == "__main__":
    V, E = map(int, input().split())
    listaAdj = [[] for _ in range(V)]

    for _ in range(E):
        de, para = map(int, input().split())
        addLista(listaAdj, de - 1, para - 1)

    resultado = bipartirGrafoDFS(listaAdj, V)
    if resultado == "IMPOSSIBLE":
        print("IMPOSSIBLE")
    else:
        print(" ".join(map(str, resultado)))