from collections import defaultdict
import heapq


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        # ---------------------- DIJKSTRA ----------------------
        # weight graph
        # u -> {v -> w , v -> w}
        # 2 -> {1 -> 1, 3-> 1 }
        # 3 -> {4 -> 1}
        weight = defaultdict(dict)
        for u, v, w in times:
            weight[u][v] = w

       #heap = [(time, vertice)]
        heap = [(0, k)]
        dist = {}

        while heap:
            time, u = heapq.heappop(heap)
            if u not in dist:
                dist[u] = time
                for v in weight[u]:
                    #heap, (time, v)
                    heapq.heappush(heap, (dist[u] + weight[u][v], v))
        # return the maximum time from dist
        return max(dist.values()) if len(dist) == n else -1

        # -------------- Bellman Ford -----------------
        # # every distance is inf
        # dist = [float("inf") for _ in range(n)]
        # # source distance = 0
        # dist[k-1] = 0

        # graph  [[2,1,1],[2,3,1],[3,4,1]]

        # vertices -> edge | weight
        # 2        -> 1    | 1
        # 2        -> 3    | 1
        # 3        -> 4    | 1

        # u        -> v    | w

        # for _ in range(n-1):
        #     for u, v, w in times:
        #         if dist[u-1] + w < dist[v-1]:
        #             dist[v-1] = dist[u-1] + w
        # return max(dist) if max(dist) < float("inf") else -1
