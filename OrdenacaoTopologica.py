#ordenação topológica só acontece em DAG
def addAresta (listaAdj, de, para):
    listaAdj[de].append(para)

def DFS(listaAdj, V):
    cor = ["BRANCO"] * V
    pred = [None] * V
    d = [0] * V
    f = [0] * V
    tempo = [0]
    ordemTopologica = []

    for u in range(V):
        if cor[u] == "BRANCO":
            visitaDFS(listaAdj, u, cor,  pred, d, f, tempo, ordemTopologica)
    
    ordemTopologica.reverse()
    return ordemTopologica

def visitaDFS(listaAdj, u, cor,  pred, d, f, tempo, ordemTopologica):
    cor[u] = "CINZA"
    tempo[0] += 1
    d[u] = tempo[0]

    for v in listaAdj[u]:
        if cor[v] == "BRANCO":
            pred[v] = u
            visitaDFS(listaAdj, v, cor, pred,d,f, tempo, ordemTopologica)
    
    cor[u] = "PRETO"
    tempo[0] += 1
    f[u] = tempo[0]
    ordemTopologica.append(u + 1)

if __name__ == "__main__":
    V, E = map(int, input().split())
    listaAdj = [[] for _ in range(V)]

    for _ in range(E):
        de, para = map(int, input().split())
        addAresta(listaAdj, de -1, para - 1)
    
    ordem = DFS(listaAdj, V)
    print(ordem)
