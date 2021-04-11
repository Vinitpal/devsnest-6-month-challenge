# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, node, k):

        one, two = node, node

        for i in range(k):
            two = two.next
        
        while two.next:
            one, two = one.next, two.next
        return one.val

