from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq, heap = Counter(nums), []
        
        # making tuple of (el, count) 
        for el, count in freq.items():
            # pushing count and el in heap
            heapq.heappush(heap, (count, el))
            # if heap exceeds "K" then remove the ele with minimum count
            if len(heap)==k+1:
                heapq.heappop(heap)
        # in the end, return the count of x elements in heap
        return [x[1] for x in heap]