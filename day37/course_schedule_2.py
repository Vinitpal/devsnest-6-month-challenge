from collections import defaultdict


class Solution:
    def findOrder(self, n: int, preq: List[List[int]]) -> List[int]:
        graph = [[0, set()] for x in range(n)]

        for d, s in preq:
            graph[s][1].add(d)
            graph[d][0] += 1

        q = [x for x in range(n) if graph[x][0] == 0]

        order = []

        while len(q):
            node = q.pop(0)
            order.append(node)

            for adjNode in graph[node][1]:
                if graph[adjNode][0] == 1:
                    q.append(adjNode)
                else:
                    graph[adjNode][0] -= 1
        return [] if len(order) != n else order


#         def hasCycle(u):
#             if u in resStack:
#                 return True
#             if u in visited:
#                 return False

#             visited.add(u)
#             resStack.add(u)

#             for v in graph[u]:
#                 if hasCycle(v):
#                     return True
#             ans.append(u)
#             resStack.remove(u)
#             return False

#         # made graph
#         graph = defaultdict(list)
#         for u, v in preq:
#             graph[v].append(u)


#         ans = []
#         visited = set()
#         resStack = set()

#         for u in range(numCourses):
#             if u not in visited:
#                 if hasCycle(u):
#                     return [ ]
#         return ans[::-1]
