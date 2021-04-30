# Algorithm: 

# 1) Create the graph using the given number of edges and vertices.

# 2) Create a recursive function that that current index
#    or vertex, visited and recursion stack.

# 3) Mark the current node as visited and also mark 
#    the index in recursion stack

# 4) Find all the vertices which are not visited 
#    and are adjacent to the current node.
#    Recursively call the function for those vertices, 
#    If the recursive function returns true return true.

# 5) If the adjacent vertices are already marked 
#    in the recursion stack then return true.

# 6) Create a wrapper class, that calls the recursive function 
#    for all the vertices and if any function returns true, return true.

# 7) Else if for all vertices the function returns false return false.


from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def isCyclic(self):
        visited = set()
        for u in list(self.graph):
            if u not in visited:
                if self.isCyclic_util(u, visited, -1):
                    return True
        return False

    def isCyclic_util(self, u, visited, parent):
        visited.add(u)
        for v in self.graph[u]:
            if v not in visited:
                # if the node is not in visited then recursion
                if self.isCyclic_util(v, visited, u):
                    return True
                # if a node is visited and not parent of its 
                # current vertex then there is a cycle
                elif parent != v:
                    return True
        return False
                
g = Graph()
g.addEdge(1, 0)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(0, 3)
g.addEdge(3, 4)

if g.isCyclic():
    print("Graph contains cycle")
else:
    print("Graph has no cycle")


