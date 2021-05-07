def getallpaths(src, graph, n):
    if src == n-1:
        return [[n-1]]

    paths = []

    for e in graph[src]:
        paths.extend([[src] + x for x in getallpaths(e, graph, n)])
    return paths


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        return getallpaths(0, graph, len(graph))
