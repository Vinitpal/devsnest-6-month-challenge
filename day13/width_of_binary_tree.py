# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def getWidth(root, rootlevel, rootIndex, widthMap):
    if root:
        if rootlevel not in widthMap:
            widthMap[rootlevel] = [rootIndex, rootIndex]
        elif rootIndex < widthMap[rootlevel][0]:
            widthMap[rootlevel][0] = rootIndex
        elif rootIndex > widthMap[rootlevel][1]:
            widthMap[rootlevel][1] = rootIndex
            
        getWidth(root.left, rootlevel+1, (2*rootIndex)+1, widthMap)
        getWidth(root.right, rootlevel+1, (2*rootIndex)+2, widthMap)
        
        
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        widthMap = {}
        getWidth(root, 0, 0, widthMap)
        return max([1 + x[1] - x[0] for x in widthMap.values()])