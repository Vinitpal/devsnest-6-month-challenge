# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return root
        
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            # if root have no right children
            if not root.right:
                return root.left
            # if root have no left children
            if not root.left:
                return root.right
            # if root have both left and right children
            # we replace its value with minimum node in right children
            temp = root.right
            min = temp.val
            
            # traversed till end of left child
            # becoz ofc that would be the minimum node in right children
            while temp.left:
                temp = temp.left
                min = temp.val
            root.val = min #replaced value
            # delete the minimum node in right subtree
            root.right = self.deleteNode(root.right, root.val) 
        return root