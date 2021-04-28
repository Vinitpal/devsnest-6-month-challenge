# graph = { "a" : ["c"],
#           "b" : ["c", "e"],
#           "c" : ["a", "b", "d", "e"],
#           "d" : ["c"],
#           "e" : ["c", "b"],
#           "f" : []
#         } 

from collections import defaultdict

class Graph:
    def __init__(self):

        # default dictionary to store graph
        self.graph = defaultdict(list)

    # add edge in 1 direction
    def addEdge(self, u, v):
        self.graph[u].append(v)
    
    # function to do dfs traversel
    def dfs(self, u):

        # create a set to store visited vertices
        visited = set()

        # call dfs util and print in dfs order
        self.dfs_util(u, visited)

    # function used by dfs
    def dfs_util(self, u, visited):

        # mark current node as visited
        # and print it
        visited.add(u)
        print(u, end=" ")

        # recur for all vertices
        # adjacent to this vertex
        for v in self.graph[u]:
            if v not in visited:
                self.dfs_util(v, visited)

g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print("Following is DFS from (starting from vertex 2)")
g.dfs(0)