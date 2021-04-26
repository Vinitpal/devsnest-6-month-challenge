# A graph is a data structure that consists 
# of the following two components:

# -> Nodes (a,b,c,d)
# -> edges (ab, ac, ad, bc, bd, cd)

# now edges may also include its weight/cost/value
 
# suppose we have 4 nodes (a,b,c,d)
# so those four nodes could be connected like this
# (ab, ac, ad, bc, bd, cd)

# the connection between nodes are called as edges

# edges can have any specific direction or
# it may points in both the ways 

# The following two are most common way
# to represent a graph

# -> Adjacency Matrix
# -> Adjacency List

# --------------------------------------------------
#                 ADJACENCY MATRIX
# --------------------------------------------------

# Adjacency matrix is a 2D arr of size V*V
# where V is number of vertices in graph

# let arr[i][j] = [[]]

# if arr[i][j] = 1
# then this means that there is an edge from 
# vertex i to vertex j

# if our edge has weight/value/cost then
# it can be represented as
# arr[i][j] = 7
# this means that there is an edge from
# vertex i to vertex j with a weight of 7

# Diagram of Adjacency matrix, its in 1st page
# https://jamboard.google.com/d/1ase37pRJwl_UfFuJ2gWVRHV86r8bAyU0PNTu00Zz9hE/edit?usp=sharing

# --------------------------------------------------
#                 ADJACENCY LIST
# --------------------------------------------------

# An array/list is used to store vertices and edge
# [(vertices), (edge, weight)] 