# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        setattr(ListNode, "__lt__", lambda self, other : self.val <= other.val)
        heap = []
        
        for head in lists:
            if head:
                heapq.heappush(heap, head)
        ans = ListNode(None)
        p = ans
        while len(heap) > 0:
            n = heapq.heappop(heap)
            p.next = n
            p = n
            if n.next:
                heapq.heappush(heap, n.next)
        return ans.next