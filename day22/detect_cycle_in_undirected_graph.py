#        0  1  2  3  4  5  6
adj =  [[0, 1, 0, 0, 0, 1, 0], #0
        [0, 0, 1, 0, 0, 0, 0], #1
        [0, 0, 0, 1, 0, 0, 0], #2
        [0, 0, 0, 0, 0, 1, 0], #3
        [0, 0, 0, 0, 0, 0, 0], #4
        [0, 0, 0, 0, 0, 0, 1], #5
        [0, 0, 0, 1, 0, 0, 0]] #6

def detect_cycle_in_undirected_graph(adj):
    q = [0]
    visited = set([0])
    while len(q) > 0:
        c = q.pop(0)
        for j in range(len(adj[0])):
            if adj[c][j] == 1:
                if j not in visited:
                    print(j)
                    visited.add(j)
                    q.append(j)
                else:
                    print("found cycle at node", c, j)
                    return True
    print("no cycle")
    return False    

detect_cycle_in_undirected_graph(adj)