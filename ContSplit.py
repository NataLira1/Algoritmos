def Cont (A):
    n = len(A)
    if (n == 1):
        return 0
    else: 
        q = (n) // 2
        x = Cont(A[:q])
        y = Cont(A[q:])
        z = ContSplit(A, 0, q - 1, n -1)
    return x + y + z

def ContSplit(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    L = [0] * (n1)
    R = [0] * (n2)
    for i in range(0, n1):
        L[i] = arr[l + i]

    for j in range(0, n2):
        R[j] = arr[m + 1 + j]
    i = 0     # Initial index of first subarray
    j = 0     # Initial index of second subarray
    k = l     # Initial index of merged subarray
    count = 0

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            count += n1 - i
            j += 1
        k += 1
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

    return count

teste = [8,3,2,9,7,1,5,4]

resultado = Cont(teste)

print(resultado)
