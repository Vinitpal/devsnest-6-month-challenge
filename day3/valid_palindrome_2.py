class Solution:
    def validPalindrome(self, s: str) -> bool:
        ##left, right pointers
        l, r = 0, len(s)-1
        
        while l < r+1:
            if s[l] != s[r]:
                one, two = s[l:r], s[l+1: r+1]
                return one == one[::-1] or two == two[::-1]
            else:
                l += 1
                r -= 1
        return True
        