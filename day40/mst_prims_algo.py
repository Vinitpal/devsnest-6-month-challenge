""" Prims Algorithm """
#        0 , 1 , 2 , 3 , 4 , 5 , 6 , 7
adj = [[0, 10, 0, 0, 0, 100, 0, 120],
       [10, 0, 130, 0, 0, 0, 0, 20],
       [0, 130, 0, 150, 0, 0, 30, 140],
       [0, 0, 150, 0, 60, 0, 70, 0],
       [0, 0, 0, 60, 0, 50, 80, 0],
       [100, 0, 0, 0, 50, 0, 40, 110],
       [0, 0, 30, 70, 80, 40, 0, 90],
       [120, 20, 140, 0, 0, 110, 90, 0]]

"""                     100
                (0)------------(5)
               / |           /  | \
              /  |         /    |  \
          10 /   |120    /110   |40 \50
            /    |     /        |    \
           /  20 |   /   90     |  80 \
        (1)------(7)----------(6)------(4)
          \      |          /   |     /
           \     |        /     |    /
         130\    |140   /30   70|   /60
             \   |    /         |  /
              \  |  /           | /
               (2)-------------(3)
               
"""
v = len(adj)
inf = float('inf')
dist = {x: inf for x in range(v)}

start = 1
dist[start] = 0
visited = [False]*v
path = []

for i in range(v):
    min_edge = inf
    x = -1
    for j in range(v):
        if not visited[j] and dist[j] < min_edge:
            x = j
            min_edge = dist[j]
    path.append(min_edge)
    visited[x] = True
    for j in range(v):
        if not visited[j] and adj[x][j] > 0:
            dist[j] = min(dist[j], adj[x][j])

path.pop(0)
print("Path's edges, those have been taken ~ ", path)
print("Minimum path sum = ", sum(path))
# Minimum path sum = sum(dist.values())
