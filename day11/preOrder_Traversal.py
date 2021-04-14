# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        # Using recursion
        # ans = []
        # self.preorder(root, ans)
        # return ans
    
    # def preorder(self, root, ans):
    #     if root:
    #         ans.append(root.val)
    #         self.preorder(root.left, ans)
    #         self.preorder(root.right, ans)
            
        # Using Iteration
            ans = []
            stack = []
            
            stack.append(root)
            while stack:
                curr = stack.pop()
                if curr:
                    ans.append(curr.val)
                    stack.append(curr.right)
                    stack.append(curr.left)
            return ans