def add_vertice(adj, i, j):
    adj[i].append(j)
    adj[j].append(i) #não direcionado

def display_adj_list(adj):
    for i in range(len(adj)):
        print(f"{i}: ", end="")
        for j in adj[i]:
            print(j, end=" ")
        print()

V = 4
adj = [[] for _ in range(V)]

add_vertice(adj, 1, 0)
add_vertice(adj, 1, 2)
add_vertice(adj, 2, 0)

display_adj_list(adj)

#lista é preferivel para grafos esparços