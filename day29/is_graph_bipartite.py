class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:

        # ---------------- DFS ------------------
        
        
        def dfs(u, c, col):
            col[u] = c
            
            for v in graph[u]:
                if col[v] == -1:
                    if dfs(v, c^1,col) == False:
                        return False
                elif col[u] == col[v]:
                        return False
            return True
        
        n = len(graph)
        col = [-1]*n
        
        for i in range(n):
            if col[i] == -1:
                if not dfs(i,1,col):
                    return False
        
        return True