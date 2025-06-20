import heapq
import sys
input = sys.stdin.read

def prim(n, adj):
    visited = [False] * n
    min_edge = [float('inf')] * n
    min_edge[0] = 0
    heap = [(0, 0)]
    total_cost = 0
    count = 0

    while heap:
        cost, u = heapq.heappop(heap)
        if visited[u]:
            continue
        visited[u] = True
        total_cost += cost
        count += 1

        for v, peso in adj[u]:
            if not visited[v] and peso < min_edge[v]:
                min_edge[v] = peso
                heapq.heappush(heap, (peso, v))

    return total_cost if count == n else "IMPOSSIBLE"

def main():
    data = input().split()
    n = int(data[0])
    m = int(data[1])
    adj = [[] for _ in range(n)]
    idx = 2

    for _ in range(m):
        u = int(data[idx]) - 1
        v = int(data[idx + 1]) - 1
        c = int(data[idx + 2])
        adj[u].append((v, c))
        adj[v].append((u, c))
        idx += 3

    print(prim(n, adj))

if __name__ == "__main__":
    main()
