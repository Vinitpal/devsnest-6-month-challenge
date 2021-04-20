#User function Template for python3

'''
class Node:
    def __init__(self, val, k):
        self.right = None
        self.data = val
        self.left = None
        self.key = k
'''
class Solution:
    # returns the inorder successor of the Node x in BST (rooted at 'root')
    def inorderSuccessor(self, root, x):
        # Code here
        if not root:
            return root
        if root.data == x.data:
            curr = root.right
            if not curr:
                return curr
            while curr.left:
                curr = curr.left
            return curr
        if root.data > x.data:
            ans = self.inorderSuccessor(root.left, x)
            return ans if ans else root
        return self.inorderSuccessor(root.right, x)
        
