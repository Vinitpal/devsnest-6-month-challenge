class Solution:
    def solveSudoku(self, arr):
        def isrowsafe(arr, row, num):
            for i in range(9):
                if arr[row][i] == num:
                    return False                
            return True

        def iscolsafe(arr, col, num):
            for i in range(9):
                if arr[i][col] == num:
                    return False
            return True
        
        def isboxsafe(arr, row, col, num):
            for i in range(3):
                for j in range(3):
                    if arr[i + row][j + col] == num:
                        return False
            return True
    
        def isempty(arr):
            for i in range(9):
                for j in range(9):
                    if arr[i][j] == ".":
                        return [i, j]
            return False
        
        def issafe(arr, row, col, num):
            return isrowsafe(arr, row, num) and iscolsafe(arr, col, num) and isboxsafe(arr, row-row%3, col-col%3, num)
        
        def solve(arr):
            l = isempty(arr)
            if not l:
                return True
            
            for i in range(1, 10):
                if issafe(arr, l[0], l[1], str(i)):
                    arr[l[0]][l[1]] = str(i)
                    
                    if solve(arr):
                        return True
                    
                    arr[l[0]][l[1]] = "."
            return False
        
        solve(arr)
            
        