class Solution:
    def myPow(self, x: float, n: int) -> float:
        isnNeg, isxNeg = n<0, x<0
        x,n = abs(x), abs(n)
        
        if n == 0:
            return 1
        if n == 1:
            return 1/x if isnNeg else x
        
        pwr = self.myPow(x, n//2)
        ans = pwr*pwr if n%2 == 0 else pwr*pwr*x
        
        if isxNeg and n%2==1:
            ans = -ans
        if isnNeg:
            ans = 1/ans
        
        return ans
        