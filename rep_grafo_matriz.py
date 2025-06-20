def addVertice(matriz, de, para):
    matriz[de][para] = 1

def displayMatriz(mat):

    for linha in mat:
        print(" ".join(map(str, linha)))

if __name__ == "__main__":
    V = 6
    mat = [[0] * V for _ in range(V)]

    addVertice(mat, 0, 1)
    addVertice(mat, 0, 3)
    addVertice(mat, 1, 4)
    addVertice(mat, 2, 4)
    addVertice(mat, 2, 5)
    addVertice(mat, 3, 1)
    addVertice(mat, 4, 3)
    addVertice(mat, 5, 5)

    displayMatriz(mat)