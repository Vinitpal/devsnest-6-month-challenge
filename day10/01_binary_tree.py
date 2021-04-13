# A Class that represents an individual node 
# in a Binary Tree 

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# creating simple tree

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)

print(root.data)