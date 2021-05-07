class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        e1, e2 = edges[0]
        return e1 if e1 in edges[1] else e2
