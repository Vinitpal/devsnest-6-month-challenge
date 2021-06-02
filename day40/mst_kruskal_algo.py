'''
## What is Minimum Spanning Tree?

-> Given a connected and undirected graph, a "spanning tree" of that graph is a subgraph that is a tree and connects all the vertices together.

-> There can be many spanning trees but a MST is a spanning tree with weight less than or equal to the weight of every other spanning tree.

->A MST has v-1 edges where v is the number of vertices in the given graph.

## 
'''

# code to find MST using kruskal's algorithm

from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.V = vertices  # no. of vertices
        self.graph = []

    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    # a function to find set of element i
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    # a function that does union of two sets of
    # x and y
    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        # Attach smaller rank tree under root of
        # higher rank tree
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[yroot] < rank[xroot]:
            parent[yroot] = xroot
        else:  # if both have same rank
            parent[yroot] = xroot
            rank[xroot] += 1

    # function to construc MST using kruskal algo
    def MST(self):
        result = []  # store resultant MST

        # index var, used for sorted edges
        i = 0

        # index var, used for result[]
        e = 0

        # sort all the edges in non-decreasing
        # order of their weight.
        self.graph = sorted(self.graph, key=lambda item: item[2])

        parent = []
        rank = []

        # create subsets with all elements
        # in graph and their rank as zero
        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        while e < self.V-1:
            # pick the smallest edge and
            # increment the index i
            u, v, w = self.graph[i]
            i += 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            # if there is no cycle then append
            # it in result and increment the
            # index e
            if x != y:
                e = e+1
                result.append([u, v, w])
                self.union(parent, rank, x, y)

        minimumCost = 0
        print("Edges in constructed MST")
        for u, v, weight in result:
            minimumCost += weight
            print("%d --- %d == %d" % (u, v, weight))
        print("Minimum spanning tree cost", minimumCost)

# Driver code
g = Graph(4)
g.addEdge(0, 1, 10)
g.addEdge(0, 2, 6)
g.addEdge(0, 3, 5)
g.addEdge(1, 3, 15)
g.addEdge(2, 3, 4)
 
# Function call
g.MST()