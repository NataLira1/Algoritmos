def mochila(N, W, pesos, valores):
    dp = [0] * (W + 1)

    for i in range(N):
        peso = pesos[i]
        valor = valores[i]
        for j in range(W, peso - 1, -1):
            dp[j] = max(dp[j], dp[j - peso] + valor)
    return dp[W]

N, W = map(int, input().split())
pesos = []
valores = []

for _ in range(N):
    w, v = map(int, input().split())
    pesos.append(w)
    valores.append(v)

print(mochila(N, W, pesos, valores))