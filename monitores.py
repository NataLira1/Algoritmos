import sys
sys.setrecursionlimit(3000)

def addLista(listaAdj, de, para):
    listaAdj[de].append(para)

def dfs(u, listaAdj):
    max_depth = 0
    for v in listaAdj[u]:
        max_depth = max(max_depth, dfs(v, listaAdj))
    return max_depth + 1

if __name__ == "__main__":
    n = int(input())
    listaAdj = [[] for _ in range(n)]

    mentorIndependente = []
    for i in range(n):
        pi = int(input())
        if pi == -1:
            mentorIndependente.append(i)
        else: 
            addLista(listaAdj, pi - 1, i)


    profundidade_maxima = 0
    for mentor in mentorIndependente:
        profundidade_maxima = max(profundidade_maxima, dfs(mentor, listaAdj))

    print(profundidade_maxima)