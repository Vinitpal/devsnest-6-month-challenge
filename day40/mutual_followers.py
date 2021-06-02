from collections import defaultdict


class Solution:
    def solve(self, relations):
        ans = set()
        vis = set()

        for u, v in relations:
            vis.add((u, v))

            if (v, u) in vis:
                ans.add(v)
                ans.add(u)

        return list(ans)
