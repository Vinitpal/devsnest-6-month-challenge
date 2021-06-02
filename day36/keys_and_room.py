class Solution:
    def canVisitAllRooms(self, graph: List[List[int]]) -> bool:
        non_vis = set([i for i in range(len(graph))])

        q = [non_vis.pop()]

        while len(q) > 0:

            i = q.pop(0)

            for x in graph[i]:
                if x in non_vis:
                    q.append(x)
                    non_vis.remove(x)
        return not len(non_vis)
