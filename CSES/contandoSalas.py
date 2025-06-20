import sys
from collections import deque
sys.setrecursionlimit(10**6)  # Aumenta o limite de recursão (não será necessário com a abordagem iterativa)

def displayMatriz(mat):
    for linha in mat:
        print(" ".join(map(str, linha)))

def contandoSalas(matriz, linhas, colunas):
    def dfs_iterativo(x, y):
        # Usa uma pilha para simular a DFS
        stack = deque([(x, y)])
        while stack:
            cx, cy = stack.pop()
            if cx < 0 or cx >= linhas or cy < 0 or cy >= colunas or matriz[cx][cy] == 0:
                continue
            # Marca a célula como visitada
            matriz[cx][cy] = 0
            # Adiciona as células vizinhas à pilha
            stack.append((cx - 1, cy))  # cima
            stack.append((cx + 1, cy))  # baixo
            stack.append((cx, cy - 1))  # esquerda
            stack.append((cx, cy + 1))  # direita

    contando = 0

    for l in range(linhas):
        for c in range(colunas):
            if matriz[l][c] == 1:  # Encontrou um agrupamento
                contando += 1
                dfs_iterativo(l, c)  # Marca todo o agrupamento como visitado

    return contando

if __name__ == "__main__":
    linhas, colunas = map(int, input().split())
    matrizAdj = [[0] * colunas for _ in range(linhas)]
    for i in range(linhas):
        itens = list(input())
        col = 0
        for item in itens:
            if item == '#':
                matrizAdj[i][col] = 0
            elif item == '.':
                matrizAdj[i][col] = 1
            col += 1
    print(contandoSalas(matrizAdj, linhas, colunas))