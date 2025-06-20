import sys
input = sys.stdin.readline

class DisjointSetUnion:
    def __init__(self, num_nodes: int) -> None:
        self.parent = [*range(num_nodes)]
        self.size = [1] * num_nodes

    def find_parent(self, v: int) -> int:
        if self.parent[v] == v:
            return v
        self.parent[v] = self.find_parent(self.parent[v])
        return self.parent[v]

    def union(self, a: int, b: int) -> bool:
        a = self.find_parent(a)
        b = self.find_parent(b)
        if a == b:
            return False
        if self.size[a] < self.size[b]:
            a, b = b, a
        self.parent[b] = a
        self.size[a] += self.size[b]
        return True

    def connected(self, a: int, b: int) -> bool:
        return self.find_parent(a) == self.find_parent(b)

n, m = map(int, input().split())

cidades = DisjointSetUnion(n)
max_tamanho = 1
components = n

for _ in range(m):
    a, b = map(lambda i: int(i) - 1, input().split())
    if cidades.union(a, b):
        components -= 1
    size_a = cidades.size[cidades.find_parent(a)]
    if size_a > max_tamanho:
         max_tamanho = size_a

    print(components, max_tamanho)
