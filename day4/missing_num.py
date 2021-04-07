class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        x = len(nums)
        for i in range(len(nums)):
            x = x^nums[i]
            x = x^i
        return x
            