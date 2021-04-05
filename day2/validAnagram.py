class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # s = "anagram"
        # t = "nagaram"
        # s-map, t-map
        sm, tm = {}, {}
        
        for c in s:
            if c not in sm:
                sm[c] = 1
            else:
                sm[c] += 1
        
        for c in t:
            if c not in tm:
                tm[c] = 1
            else:
                tm[c] += 1
        
        if len(sm) != len(tm):
            return False
        
        return sm == tm
