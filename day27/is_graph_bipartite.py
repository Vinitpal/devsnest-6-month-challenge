class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:

        # ---------------- DFS ------------------
        
        # nahi ban rha
        
        # ---------------- BFS ------------------
        
        def solve(color, u, graph):
            color[u] = 1
            q = [u]
            while q:
                c = q.pop(0)
                for v in range(len(graph)):
                    if v in graph[c]:
                        if color[c] == color[v]:
                            return False
                        elif color[v] == -1:
                            color[v] = 1 - color[c]
                            q.append(v)
            return True        
        n = len(graph)
        color = [-1]*n
        
        for i in range(n):
            if color[i] == -1:
                if not solve(color, i, graph):
                    return False
        return True
