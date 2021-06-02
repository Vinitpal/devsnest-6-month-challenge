from collections import defaultdict


class Solution:
    def canFinish(self, n: int, preq: List[List[int]]) -> bool:
        graph = [[0, set()] for x in range(n)]

        for d, s in preq:
            graph[s][1].add(d)
            graph[d][0] += 1

        q = [x for x in range(n) if graph[x][0] == 0]
        count = n

        while len(q):
            nodeid = q.pop(0)
            count -= 1

            for i in graph[nodeid][1]:
                if graph[i][0] == 1:
                    q.append(i)
                else:
                    graph[i][0] -= 1
        return count == 0
