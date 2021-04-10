# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
    
class Solution: 
    def middleNode(self, head: ListNode) -> ListNode:

        # INITUATIVE APPROACH
        
        # length = self.length(head)
        # midIndex = length//2 

        # p = head
        # for i in range(midIndex):
        #     p = p.next
        # return p

    # def length(self, head):
    #     count = 0
    #     temp = head
    #     while temp:
    #         count += 1
    #         temp = temp.next
    #     return count
    
        # OPTIMISED APPROACH USING 2 POINTERS
        
        fast, slow = head.next, head
        
        if not fast:
            return head
        
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        
        return slow.next