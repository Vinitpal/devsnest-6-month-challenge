# Following is detailed Kosaraju’s algorithm :

# 1) Create an empty stack ‘Stack’ and do DFS traversal of a graph.
#    Push node to stack before returning.  
# 2) Find the transpose graph by reversing the edges.
# 3) pop nodes one by one from stack
#    and again do dfs on modified graph -> each succesful dfs will give one scc 

from collections import defaultdict

class Graph:

    def __init__(self, vertices):
        self.V = vertices # no. of vertices
        self.graph = defaultdict(list)
    