# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, node):
        ans = node
        while node:
            k = node
            val = k.val
            while val > 0 and node:
                node = node.next
                val -= 1 
            k.next = node
        return ans