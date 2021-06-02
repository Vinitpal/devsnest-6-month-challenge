# # Union find algorithm in short

# def find(parent, i):
#     if parent[i] == -1:
#         return i
#     return find(parent, parent[i])

# def union(parent, x, y):
#     xset = find(parent, x)
#     yset = find(parent, y)
#     parent[xset] = yset


# Python Program for union-find algorithm to detect cycle in a undirected graph

# we have one egde for any two vertex i.e 1-2 is either 1-2 or 2-1 but not both

from collections import defaultdict

# class to make adj list


class Graph:
    def __init__(self, vertices):
        self.V = vertices  # no. of vertices
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    # A utility function to find the subset of an element i
    def find_parent(self, parent, i):
        if parent[i] == -1:
            return i
        if parent[i] != -1:
            return self.find_parent(parent, parent[i])

    # A utility function to do union of two subsets
    def union(self, parent, x, y):
        parent[x] = y

    def isCyclic(self):
        # everyone's parent is -1
        parent = [-1]*self.V

        # Iterate through all edges of graph, find subset of both
        # vertices of every edge, if both subsets are same, then
        # there is cycle in graph.
        for i in self.graph:
            for j in self.graph[i]:
                x = self.find_parent(parent, i)
                y = self.find_parent(parent, j)
                if x == y:
                    return True
                self.union(parent, x, y)


# Create a graph
g = Graph(3)
g.addEdge(0, 1)
g.addEdge(1, 2)
g.addEdge(2, 0)

if g.isCyclic():
    print("Graph contains a cycle")
else:
    print("No cycle")
