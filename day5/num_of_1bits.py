class Solution:
    def hammingWeight(self, n: int) -> int:
        # approach 1 #TC -> O(1) 
        # count = 0
        # mask = 1
        
        # for i in range(32):
        #     if (n & mask) != 0:
        #         count += 1
        #     mask = mask << 1
        # return count
    
        # approach 2 #TC -> O(1)
        # count = 0
        # while n != 0:
        #     n = n & (n-1)
        #     count+=1
        # return count
        
        # approach 2 with recursion
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        return self.hammingWeight(n&(n-1)) + 1