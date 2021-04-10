# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def cutinhalf(head):
    fast, slow = head.next, head

    if not fast:
        return fast
    
    while fast.next and fast.next.next:
        fast = fast.next.next
        slow = slow.next

    if fast.next:
        slow = slow.next
    k = slow.next
    slow.next = None
    return k

def reverse(head):
    if not head or not head.next:
        return head
    p = head
    c = head.next
    n = head.next.next
    
    p.next = None
    while n:
        c.next = p
        p = c
        c = n
        n = n.next
    c.next = p
    return c

class Solution:
    def reorderList(self, head: ListNode) -> None:
        
        # cut head from half and reversed it
        h = cutinhalf(head)
        h = reverse(h)
        
        p = head
        while p and h:
            h2 = h.next
            h.next = p.next
            p.next = h
            
            p = p.next.next
            h = h2
        return head
        