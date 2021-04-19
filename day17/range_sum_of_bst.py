 class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        # how i started my initution, it gives error but anyways
        
        # if root is None:
        #     return 0
        
        # ans = 0
        # # print(root.val)

        # if (low <= root.val) and (root.val <= high):
        #     ans = root.val
        #     print(root.val)
        # self.rangeSumBST(root.left, low, high)
        # self.rangeSumBST(root.right, low, high)
        # return ans
 
        # after thinking a lot
        if root is None:
            return 0
        
        l = self.rangeSumBST(root.left, low, high)
        r = self.rangeSumBST(root.right, low, high)
        
        if low > root.val:
            return r
        if high < root.val:
            return l
        return root.val + l + r