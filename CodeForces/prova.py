import sys
sys.setrecursionlimit(10**6)

def addLista(listaAdj, de, para):
    listaAdj[de].append(para)
    listaAdj[para].append(de)

def topologicaBarramento(grausEntrada, V):

    variavel = 0
    entrou = False
    for graus in grausEntrada:
        if graus == 1:
            variavel += 1
            entrou = True

        if graus == 2:
            variavel += 1
    if variavel == V and V != 0 and entrou:
        return True 
    else:
        return False

def topologiaAnel(grausEntrada, V):
    variavel = 0

    for graus in grausEntrada:
        if graus == 2:
            variavel += 1

    if variavel == V and V != 0:
        return True
    else:
        return False

def topologiaEstrela(grausEntrada, V):
    variavel = 0
    entrou = False

    for graus in grausEntrada:
        if graus == V - 1:
            variavel += 1
            entrou = True
        if graus == 1:
            variavel += 1
            entrou = True

    if variavel == V and entrou and V != 0:
        return True
    else:
        return False
    
if __name__ == "__main__":

    V, A = map(int, input().split())
    listaAdj = [[] for _ in range(V)]
    grausEntrada = [0] * V

    for _ in range(A):
        de, para = map(int, input().split())
        addLista(listaAdj, de - 1, para - 1)
        grausEntrada[para- 1] += 1 
        grausEntrada[de-1] += 1

    if(topologicaBarramento(grausEntrada, V)):
        print("bus topology")
    elif (topologiaEstrela(grausEntrada, V)):
        print("star topology")
    elif (topologiaAnel(grausEntrada, V)):
        print("ring topology")
    else:
        print("unknown topology")
