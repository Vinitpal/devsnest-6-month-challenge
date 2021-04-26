#        0  1  2  3  4  5  6
adj =  [[0, 1, 0, 0, 0, 1, 0], #0
        [0, 0, 1, 0, 0, 0, 0], #1
        [0, 0, 0, 1, 0, 0, 0], #2
        [0, 0, 0, 0, 0, 1, 0], #3
        [0, 0, 0, 0, 0, 0, 0], #4
        [0, 0, 0, 0, 0, 0, 1], #5
        [0, 0, 0, 1, 0, 0, 0]] #6

def print_bfs(adj, curr):
    q = [curr]
    visited = set([curr]) 
    while len(q) > 0: 
        c = q.pop(0) 
        print(c)
        for j in range(len(adj[0])):
            if adj[c][j] == 1 and j not in visited: 
                visited.add(j) 
                q.append(j)

print_bfs(adj, 0)