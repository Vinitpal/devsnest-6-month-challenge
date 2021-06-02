# https://leetcode.com/problems/longest-happy-prefix/submissions/

class Solution:
    def longestPrefix(self, s: str) -> str:
        n = len(s)
        lps = [0]
        prefix = 0
        curr = 1

        while curr < n:
            if s[curr] == s[prefix]:
                prefix += 1
                curr += 1
                lps.append(prefix)
            else:
                if prefix == 0:
                    lps.append(0)
                    curr += 1
                else:
                    prefix = lps[prefix-1]
        return s[n-lps[-1]:]
