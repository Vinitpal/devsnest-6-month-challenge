# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # Three Pointer Approach (Iteratively)
        # if not head or not head.next:
        #     return head
        # p = head
        # c = head.next
        # n = head.next.next
        
        # p.next = None
        # while n:
        #     c.next = p
        #     p = c
        #     c = n
        #     n = n.next
        # c.next = p
        # return c

        # Recursive Approach
        if not head or not head.next:
            return head

        next_node = head.next
        head.next = None
        new_node = self.reverseList(next_node)
        next_node.next = head
        return new_node
                