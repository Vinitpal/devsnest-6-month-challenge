# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, head):
        k = head
        if head.next == None:
            return True
        if head.val >= head.next.val:
            return False
        return self.solve(head.next) 