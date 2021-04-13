class Solution:
    def arraySign(self, nums: List[int]) -> int:
        ans = 1
        for i in range(len(nums)):
            ans = ans*nums[i]
        
        if ans > 0:
            return 1
        if ans < 0:
            return -1
        if ans == 0:
            return 0