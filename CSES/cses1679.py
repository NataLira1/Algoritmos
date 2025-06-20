from collections import deque

def addLista (listaAdj, de, para):
    listaAdj[de].append(para)

def ordemTopologica(listaAdj, V, grausEntrada):

    fila = deque()

    for u in range(V):
        if grausEntrada[u] == 0:
            fila.append(u)

    ordemTopologica = []

    while fila:

        u = fila.popleft()
        ordemTopologica.append(u + 1)

        for v in listaAdj[u]:
            grausEntrada[v] -= 1
            if grausEntrada[v] == 0:
                fila.append(v)

    return ordemTopologica

if __name__ == "__main__":

    V, E = map(int, input().split())
    listaAdj = [[] for _ in range(V)]
    grausEntrada = [0] * V

    for _ in range(E):
        de, para = map(int, input().split())
        addLista(listaAdj, de - 1, para - 1)
        grausEntrada[para - 1] += 1

    ordem = ordemTopologica(listaAdj, V, grausEntrada)

    if len(ordem) != V:
        print("IMPOSSIBLE")
    else:
        print(' '.join(map(str, ordem)))
    
