import sys
from collections import deque
sys.setrecursionlimit(10**6)

def encontrarCaminho(matriz, linhas, colunas):
    # Localiza as posições de A (início) e B (fim)
    inicio = fim = None
    for i in range(linhas):
        for j in range(colunas):
            if matriz[i][j] == 'A':
                inicio = (i, j)
            elif matriz[i][j] == 'B':
                fim = (i, j)
    # Verifica se início e fim foram encontrados
    if inicio is None or fim is None:
        return "NO", None, None
    # Movimentos possíveis: cima, baixo, esquerda, direita
    movimentos = [(-1, 0, 'U'), (1, 0, 'D'), (0, -1, 'L'), (0, 1, 'R')]
    # Matriz para rastrear de onde veio cada célula
    visitados = [[None] * colunas for _ in range(linhas)]
    fila = deque([inicio])
    visitados[inicio[0]][inicio[1]] = None  # Marca o início como visitado
    while fila:
        x, y = fila.popleft()
        # Se chegou ao destino, reconstrói o caminho
        if (x, y) == fim:
            caminho = []
            while (x, y) != inicio:
                px, py = visitados[x][y]
                dx, dy = x - px, y - py
                for mx, my, direcao in movimentos:
                    if mx == dx and my == dy:
                        caminho.append(direcao)
                        break
                x, y = px, py
            return "YES", len(caminho), "".join(reversed(caminho))
        # Explora os vizinhos
        for dx, dy, direcao in movimentos:
            nx, ny = x + dx, y + dy
            if 0 <= nx < linhas and 0 <= ny < colunas and matriz[nx][ny] != '#' and visitados[nx][ny] is None:
                visitados[nx][ny] = (x, y)  # Marca de onde veio
                fila.append((nx, ny))
    # Se não encontrou o caminho
    return "NO", None, None

if __name__ == "__main__":
    # Entrada
    linhas, colunas = map(int, input().split())
    matriz = [list(input().strip()) for _ in range(linhas)]

    # Processa o labirinto
    resultado, comprimento, caminho = encontrarCaminho(matriz, linhas, colunas)
    # Saída
    print(resultado)
    if resultado == "YES":
        print(comprimento)
        print(caminho)