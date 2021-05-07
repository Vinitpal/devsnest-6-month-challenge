class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        tcounts = [[0, 0] for i in range(n)]
        for t in edges:
            s, d = t[0], t[1]
            tcounts[s][1] += 1
            tcounts[d][0] += 1
        ans = []
        for k in range(n):
            inc, outg = tcounts[k]
            if inc == 0:
                ans.append(k)
        return ans
