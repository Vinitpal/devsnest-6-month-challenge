from collections import defaultdict
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        def dfs(graph, src, target, visited):
            if src not in visited:
                visited[src] = 1
                if src == target:
                    return True
                for v in graph[src]:
                    if dfs(graph, v, target, visited):
                        return True
        
        graph = defaultdict(list)

        for i in edges:
            visited = {}
            u, v = i[0], i[1]
            if u in graph and v in graph and dfs(graph, u, v, visited):
                return i
            graph[u].append(v)
            graph[v].append(u)
        
        