# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # Using recursion
        ans = []    
        self.inorder(root, ans)
        return ans
    
    def inorder(self, root, ans):
        if root:
            self.inorder(root.left, ans)
            ans.append(root.val)
            self.inorder(root.right, ans)
    
        # Using iteration
        stack = []
        ans = []
        curr = root
            
        while stack or curr:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                node = stack.pop()
                ans.append(node.val)
                curr = node.right
                
        return ans