class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # modifying nums to 3 largest ele in nums
        nums = heapq.nlargest(k, nums)
        # using heapify to maintain the minheap order 
        heapq.heapify(nums)
        self.heap = nums
        self.k = k

    def add(self, val: int) -> int:
        # pushing the new val in heap
        heapq.heappush(self.heap, val)
        # if length of heap becomes more than k 
        # then pop the mininum element in heap
        if(len(self.heap) > self.k):
            heapq.heappop(self.heap)
        # after this, our heap will have only 3 largest elements
        # so we return the kth largest element
        return self.heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)