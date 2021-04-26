# # list for undirected graph
# adj_list = {
#     "A": ["B", "C"],
#     "B": ["A", "D"],
#     "C": ["A", "D", "E"],
#     "D": ["B", "C", "E"],
#     "E": ["C", "D"]
# }

# # to print edge of any vertex
# print(adj_list["B"])

# # to add a new edge A <---> D
# adj_list["A"].append("D")
# adj_list["D"].append("A")

# print(adj_list)

# ----------------------------------------------------- #

# class for a Graph
class Graph:
    def __init__(self, Nodes, is_directed = False):
        self.nodes = Nodes
        self.adj_list = {}
        self.is_directed = is_directed

        # creates vertices from given list of nodes
        # at first all vertices have no edges
        for node in self.nodes:
            self.adj_list[node] = [] 

    # # to add a new edge A <---> D
    def add_edge(self, u, v):
        self.adj_list[u].append(v)

        # if our graph is directed then new edge 
        # would only be A ---> D, so we skip this line
        # if it is not directed then we dont skip 
        if not self.is_directed:
            self.adj_list[v].append(u)

    # a degree of a node is total number of edges in a node
    def degree(self, node):
        deg = len(self.adj_list[node])
        return deg

    # function to print the whole list
    def print_adj_list(self):
        for node in self.nodes:
            print(node, "->", self.adj_list[node])

# ----------------------------------------------------- #

nodes = ["A", "B", "C", "D", "E"]
edges = [
    ("A", "B"),
     ("A", "C"),
     ("B", "D"),
     ("C", "D"), 
     ("C", "E"),
     ("D", "E"), 
]
# # for un directed graph
# graph = Graph(nodes)

# # for directed graph 
graph = Graph(nodes, is_directed=True)

# # for adding edges
# graph.add_edge("A", "D")

# we can also use a list to add multiple edges
for u, v in edges:
    graph.add_edge(u, v)

# print adj list
graph.print_adj_list()

print("Degree of C is: ", graph.degree("C"))