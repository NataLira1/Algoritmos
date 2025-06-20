#Fazendo a representação de uma matriz de adjacência

def addVertice(mat, de, para):
    mat[de][para] = 1

def displayMatriz(mat):
    for linha in mat:
        print(" ".join(map(str, linha)))

def DFS(matriz):

    n = len(matriz)
    cor = ["BRANCO"] * n
    pred = [None] * n
    d = [0] * n
    f = [0] * n
    tempo = [0]

    for u in range(len(matriz)):
        if cor[u] == "BRANCO":
            visiteDFS(matriz ,u, tempo, cor, d,f ,pred)
    
    return pred, d, f

def visiteDFS(matriz ,u, tempo, cor, d,f ,pred):

    cor[u] = "CINZA"
    tempo[0] += 1
    d[u] = tempo[0]

    for v in adjacencia(matriz, u):
        if cor[v] == "BRANCO":
            pred[v] = u
            visiteDFS(matriz ,v, tempo, cor, d,f ,pred)
    cor[u] = "PRETO"
    tempo[0] += 1
    f[u] = tempo[0]

def adjacencia(matriz, vertice):
    lista = []

    for i in range(len(matriz[vertice])):
        if matriz[vertice][i] == 1:
            lista.append(i)
    return lista

def mostrarTemposEPredecessores(pred, d, f):
    print("\nVértice | Descoberta (d) | Término (f) | Predecessor")
    for u in range(len(d)):
        print(f"{u:^7} | {d[u]:^14} | {f[u]:^11} | {str(pred[u]) if pred[u] is not None else '-'}")

if __name__ == "__main__":
    V, E = map(int, input().split())
    matriz = [[0] * V for _ in range(V)]

    for _ in range(E):
        de, para = map(int, input().split())
        addVertice(matriz, de - 1, para - 1)

    displayMatriz(matriz)
    pred, d, f = DFS(matriz)
    mostrarTemposEPredecessores(pred, d,f)
