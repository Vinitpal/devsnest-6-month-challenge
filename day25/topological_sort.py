from collections import defaultdict

class Graph:
    def __init__(self):

        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def print_graph(self):
        for i in self.graph:
            print(i, "->", self.graph[i])

    def topological_sort(self):
        visited = set()
        stack = []

        for i in list(self.graph):
            if i not in visited:
                self.topological_sort_util(i, visited, stack)
        
        print(stack[::-1])
    
    def topological_sort_util(self, u, visited, stack):
        visited.add(u)
        for v in self.graph[u]:
            if v not in visited:
                self.topological_sort_util(v, visited, stack)
    
        stack.append(u)

g = Graph()
g.addEdge(5, 2)
g.addEdge(5, 0)
g.addEdge(4, 0)
g.addEdge(4, 1)
g.addEdge(2, 3)
g.addEdge(3, 1)
 
print ("Following is a Topological Sort of the given graph")
g.print_graph()
g.topological_sort()