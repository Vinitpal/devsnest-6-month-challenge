from collections import defaultdict

class Graph:
    def __init__(self):
        
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def connected_comp(self):
        cc = []
        visited = set()
        for i in self.graph:
            if i not in visited:
                temp = []
                cc.append(self.dfs_util(temp, i, visited))
        return cc

    def dfs_util(self, temp, u, visited):
        visited.add(u)

        temp.append(u)
        for v in self.graph[u]:
            if v not in visited:
                self.dfs_util(temp, v, visited)
        return temp

g = Graph()
g.addEdge(0, 1)
g.addEdge(1, 0)
g.addEdge(2, 3)
g.addEdge(3, 2)
g.addEdge(3, 4)
g.addEdge(4, 3)

print(g.connected_comp())
