class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
      
        if len(set(s)) == 1 or len(s) == 0:
            return len(s)
        
        # s = "ABAB"
        # k = 2

        i = 0 # pointer one
        j = 0 # pointer two
        n = len(s)
        m = 0 # maxSubString length
        maxFreq = 0
        map = {}
        
        while i<n:
            l = s[i]
            r = s[j]
            if l not in map:
                map[l] = 1
            else:
                map[l] += 1
                
            maxFreq = max(maxFreq, map[l])
            
            if m - maxFreq >= k:
                map[r] -= 1
                j += 1
            else:
                m = max(m, i-j+1) 
            i += 1 
                     
        return m