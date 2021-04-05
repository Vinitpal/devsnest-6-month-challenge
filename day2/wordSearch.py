class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #board = [
        #           ["A","B","C","E"],
        #           ["S","F","C","S"],
        #           ["A","D","E","E"]
        # ]
        #word = "ABCCED"


        n = len(board) # row 
        m = len(board[0]) # column
        
        for i in range(n):
            for j in range(m):
                if word[0] == board[i][j] and self.find(board,word,i,j, 0): 
                    return True
        return False
    
    def find(self, board, word, row, col, c): #c is count
        if c == len(word):
            return True
        if row == -1 or col == -1 or row >= len(board) or col >= len(board[0]) or word[c] != board[row][col]:
            return False
        
        temp = board[row][col]        
        board[row][col] = "*"
        
        result = self.find(board, word, row+1, col, c+1) or self.find(board, word, row-1, col, c+1) or self.find(board, word, row, col+1, c+1) or self.find(board, word, row, col-1, c+1)
                    
        board[row][col] = temp
        return result 