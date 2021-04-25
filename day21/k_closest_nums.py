import heapq
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap, res = [], []
        for i in arr:
            heapq.heappush(heap ,(abs(x-i), i))
        
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])
        res.sort()
        return res