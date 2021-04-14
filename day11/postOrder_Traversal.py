# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        # Using Recursion
        # ans = []
        # self.postorder(root, ans)
        # return ans
        
    # def postorder(self, root, ans):
    #     if root:
    #         self.postorder(root.left, ans)
    #         self.postorder(root.right, ans)
    #         ans.append(root.val)
        
        # Using Iteration
        s1 = [root]
        s2 = []
        
        while s1:
            curr = s1.pop()
            if curr:
                s2.append(curr.val)                    
                s1.append(curr.left)            
                s1.append(curr.right)
        
        s2 = s2[::-1]
        return s2
