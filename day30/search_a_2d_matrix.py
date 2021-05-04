class Solution:
    def searchMatrix(self, mat: List[List[int]], target: int) -> bool:
        r = len(mat)
        c = len(mat[0])
        
        while r >= 0:
            for i in range(c):
                if mat[r-1][i] == target:
                    return True
            r-=1
        else:
            return False