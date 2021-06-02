class Solution:
    def findCircleNum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        visited = [False]*n

        def dfs(u):
            for v in range(n):
                if matrix[u][v] == 1 and visited[v] == False:
                    visited[v] = True
                    dfs(v)

        count = 0

        for i in range(n):
            if visited[i] == False:
                dfs(i)
                count += 1
                visited[i] == True
        return count

#         n = len(isConnected)
#         parent = [i for i in range(n)]

#         count = n
#         for i in range(n):
#             for j in range(i+1, n):
#                 if isConnected[i][j] == 1:
#                     pari, parj = i, j
#                     while parent[pari] != pari:
#                         pari = parent[pari]
#                     while parent[parj] != parj:
#                         parj = parent[parj]
#                     if pari != parj:
#                         count -= 1
#                         parent[parj] = pari
#         return count
