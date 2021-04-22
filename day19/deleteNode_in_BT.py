# Given a binary tree, delete a node from it by making sure that tree shrinks from the bottom
# (i.e. the deleted node is replaced by bottom most and rightmost node).
# This is different from BST deletion. 
# Here we do not have any order among elements, so we replace with last element.

# Algorithm 
# 1. Starting at root, find the deepest and rightmost node in binary tree and node 
# which we want to delete. 
# 2. Replace the deepest rightmost node’s data with node to be deleted. 
# 3. Then delete the deepest rightmost node.

class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

# function to delete deepest leaf
def delete_deepest(root, node):
    q = []
    q.append(root)

    while len(q):
        temp = q.pop(0)
        
        if temp is node:
            temp = None
            return
        
        if temp.right:
            if temp.right is node:
                temp.right = None
                return
            else:
                q.append(temp.right)

        if temp.left:
            if temp.left is node:
                temp.left = None
                return
            else:
                q.append(temp.left)

# function to delete element in binary tree
def delete(root, key):
    if root is None:
        return None
    if root.left is None and root.right is None:
        if root.data == key:
            return None
        else: 
            return root
    
    key_node = None
    q = []
    q.append(root)

    while len(q):
        temp = q.pop(0)
        if temp.data == key:
            key_node = temp
        if temp.left:
            q.append(temp.left)
        if temp.right:
            q.append(temp.right)

    if key_node:
        x = temp.data
        delete_deepest(root, temp)
        key_node.data = x       
    return root

# Driver code
if __name__ == '__main__':
    root = TreeNode(10)
    root.left = TreeNode(11)
    root.left.left = TreeNode(7)
    root.left.right = TreeNode(12)
    root.right = TreeNode(9)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(8)

    print("The tree before the deletion:")
    inorder(root)

    key = 10
    root = delete(root, key)
    print("The Tree after the deletion:")
    inorder(root)