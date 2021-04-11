# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, node):
        fast, slow = node.next, node
    
        if not fast:
            return node

        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        return slow.next.val