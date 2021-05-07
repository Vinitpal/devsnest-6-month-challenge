# solved it again with different approach

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return 1

        tcounts = [[0, 0] for i in range(n+1)]
        for s, d in trust:
            # print(tcounts, s, d)
            # print("**********")
            tcounts[s][1] += 1
            tcounts[d][0] += 1

        for i in range(n+1):
            if tcounts[i][0] == n-1 and tcounts[i][1] == 0:
                return i
        return -1
