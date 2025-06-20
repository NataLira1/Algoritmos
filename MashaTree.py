def arvore_bonita(l, r, A):
    if l == r:
        return 0
    
    q = (l + r) //2
    x1 = arvore_bonita(l, q, A)
    x2 = arvore_bonita(q + 1, r, A)

    if x1 == -1 or x2 == -1:
        return -1
    
    y = troca(l, q, r, A)
    if y == -1:
        return -1
    
    return x1 + x2 + y

def troca(l, q, r, A):
    if A[q] <= A[q+1]:
        return 0
    else:
        if A[l] > A[r]:

            A[l:q+1], A[q+1:r+1] = A[q+1:r+1], A[l:q+1]
            return 1
        else:
            return -1
        
t = int(input())

resultado = []

for _ in range(t):
    m = int(input())
    A = list(map(int, input().split()))

    x = arvore_bonita(0, m - 1, A)
    resultado.append(x)

for i in resultado:
    print(i)