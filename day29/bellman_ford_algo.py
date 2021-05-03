adj = [
    [None, 5, 2, None, None],
    [None, None, 3, None, None],
    [None, None, None, -1, -1],
    [None, None, None, None, None],
    [3, None, None, 2, None,]
    ]

inf = 999999999999999
n = len(adj)
src = 0
dist = [inf]*n
dist[src] = 0

for _ in range(n-1):
    any_edge_updated = False
    for nodeFrom in range(n):
        for nodeTo in range(n):
            if adj[nodeFrom][nodeTo] and dist[nodeFrom] != inf and dist[nodeTo] > adj[nodeFrom][nodeTo] + dist[nodeFrom]:
                dist[nodeTo] = adj[nodeFrom][nodeTo] + dist[nodeFrom]
                any_edge_updated = True
        if not any_edge_updated:
            break

print(dist)