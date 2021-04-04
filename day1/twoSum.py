class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       # nums = [3,2,4]
       # target = 6
        
        num_map = {}
        for i, value in enumerate(nums):
            x = nums[i]
            y = target - x
            if y in num_map: 
                return [i, num_map[y]]
            else:
                num_map[value] = i