class Solution:
    def mySqrt(self, x: int) -> int:
        # return math.floor(x**0.5)

        start = 0
        end = x
        ans = start
        
        while start <= end:
            mid = (start + end)//2
            if mid*mid <= x:
                start = mid + 1
                ans = mid
            else:
                end = mid - 1
        return ans