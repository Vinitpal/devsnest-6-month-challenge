#        0  1  2  3  4  5  6
adj =  [[0, 1, 0, 0, 0, 1, 0], #0
        [0, 0, 1, 0, 0, 0, 0], #1
        [0, 0, 0, 1, 0, 0, 0], #2
        [0, 0, 0, 0, 0, 1, 0], #3
        [0, 0, 0, 0, 0, 0, 0], #4
        [0, 0, 0, 0, 0, 0, 1], #5
        [0, 0, 0, 1, 0, 0, 0]] #6

def print_dfs(adj, curr, visited):
        if curr in visited:
                return
        print(curr)
        visited.add(curr)
        for j in range(len(adj[0])):
                if adj[curr][j] == 1:
                        print_dfs(adj, j, visited)


print_dfs(adj, 0, set())


# ------------------------------------------------ #

# adj_list = {
#         "A": ["B", "C"],
#         "B": ["D", "E"],
#         "C": ["B", "F"],
#         "D": [],
#         "E": ["F"],
#         "F": []
# }


# color = {} # W G 
# dfs_output = []

# # initialize color
# for node in adj_list.keys():
#         color[node] = "W"


# def dfs_util(u):
#         # change color for visited
#         color[u] = "G"
#         dfs_output.append(u)

#         # loop to go in depth
#         for v in adj_list[u]:
#                 if color[v] == "W":
#                         dfs_util(v)

# # loop to go at each node
# for u in adj_list.keys():
#         if color[u] == "W":
#                 dfs_util(u)

# print(dfs_output)
