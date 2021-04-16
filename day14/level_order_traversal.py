# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        ans = []
        q = [root]
        while q:
            val = []
            for i in range(len(q)):
                node = q.pop(0) 
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                val.append(node.val)
            ans.append(val)
        return ans