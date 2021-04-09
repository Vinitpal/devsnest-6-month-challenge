# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        k = ListNode()
        ans = k
        
        while l1 and l2:
            if l2.val > l1.val:
                k.next = l1
                l1 = l1.next
                k = k.next
            else:
                k.next = l2
                l2 = l2.next
                k = k.next
                
        #this case applies if anyone list is of small size than other
        k.next = l1 or l2 
        
        return ans.next