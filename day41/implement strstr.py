'''
https://leetcode.com/problems/implement-strstr/
'''


class Solution:
    def strStr(self, s: str, t: str) -> int:

        # RABIN KARP METHOD

        if t not in s:
            return -1
        if len(t) > len(s):
            return -1
        if len(t) == 0:
            return 0

        a = l = len(t)
        p = 26
        hash_t = 0

        for c in t:
            hash_t += (ord(c)-100)*p**(l-1)
            l -= 1

        l = a
        i = 0
        hash_s = 0

        while l > 0:
            hash_s += (ord(s[i])-100)*p**(l-1)
            l -= 1
            i += 1
        if hash_s == hash_t:
            return i-a

        while i < len(s):
            hash_s = (hash_s - (ord(s[i-a])-100)*p**(a-1))*p + ord(s[i])-100
            i += 1
            if hash_s == hash_t:
                return i-a
        else:
            return -1
