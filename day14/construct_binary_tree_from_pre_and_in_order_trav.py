# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        
        # preIndex = 0
            if not len(inorder):
                return None
        
            n = preorder.pop(0)
            root = TreeNode(n)

            if len(inorder) == 1:
                return root 

            sp = inorder.index(n)
            left = inorder[:sp]
            right = inorder[sp+1:]

            root.left = self.buildTree(preorder, left)
            root.right = self.buildTree(preorder, right)

            return root