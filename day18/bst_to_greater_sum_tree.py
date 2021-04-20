# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def gst(root, sm):
    if not root:
        return sm #sm is sum of greater values
    
    # first we calculated sum of right most node,
    # cuz ofc it would be greatest
    sm = gst(root.right, sm)
    
    # then we kept changing the val of curr node
    root.val += sm
    # then we updated our sum
    sm = root.val
    # then we did same for left subtree
    return gst(root.left, sm)
    

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        gst(root, 0)
        return root