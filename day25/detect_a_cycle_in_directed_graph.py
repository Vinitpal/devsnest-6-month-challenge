from collections import defaultdict

class Graph():
    def __init__(self):
        self.graph = defaultdict(list)
 
    def addEdge(self , u, v):
        self.graph[u].append(v)

    def isCyclic(self):
        visited = set()
        recStack = set()

        for u in list(self.graph):
            if u not in visited:
                if self.isCyclic_util(u, visited, recStack):
                    return True
        return False
    
    def isCyclic_util(self, u, visited, recStack):
        visited.add(u)
        recStack.add(u)

        # recur for all edges
        # if any edge is in visited and 
        # in recStack then graph is cyclic
        for v in self.graph[u]:
            if v not in visited:
                if self.isCyclic_util(v, visited, recStack):
                    return True
            elif v in recStack:
                return True

        # the node needs to be poped from
        # recurStack before function ends
        recStack.remove(u)
        return False     

g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

if g.isCyclic():
    print("Graph has cycle")
else:
    print("Graph has no cycle")