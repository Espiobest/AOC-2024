from collections import defaultdict

with open('data.txt', 'r') as r:
    lines = r.read().splitlines()

graph = defaultdict(set)
for line in lines:
    a, b = line.split("-")
    # undirected graph
    graph[a].add(b)
    graph[b].add(a)

def find_triangles(graph):
    triangles = set()
    for v in graph:
        neighbors = graph[v]
        for n in neighbors:
            for m in neighbors:
                if n != m and m in graph[n]:
                    triangle = tuple(sorted((v, n, m)))
                    triangles.add(triangle)
    
    return triangles
    

triangles = find_triangles(graph)
part1 = len([triangle for triangle in triangles if any(t[0] == 't' for t in triangle)])
print("Part 1:", part1)

def choose_pivot(graph, p, x):
    max_connections = -1
    pivot = None
    
    for v in p | x:
        connections = len(set(graph[v]) & p)
        if connections > max_connections:
            max_connections = connections
            pivot = v
            
    return pivot

def bron_kerbosch(r, p, x, graph):
    if not p and not x:
        return r
    
    max_clique = r if r else set()
    pivot = choose_pivot(graph, p, x) # choose pivot with most connections

    rest = p - graph[pivot]
    for v in rest:
        neighbors = graph[v]
        new_clique = bron_kerbosch(r | {v}, p & neighbors, x & neighbors, graph)
        if len(new_clique) > len(max_clique):
            max_clique = new_clique
        
        p.remove(v)
        x.add(v)
    
    return max_clique

r = set()
p = set(graph.keys())
x = set()
max_clique = bron_kerbosch(r, p, x, graph)

part2 = ",".join(sorted(max_clique))
print("Part 2:", part2)