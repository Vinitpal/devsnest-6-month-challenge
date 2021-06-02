class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return

        r = len(board)
        c = len(board[0])

        if r <= 2 or c <= 2:
            return
        # making all borders 'O' into '#'
        for i in range(r):
            self.dfs(board, i, 0)  # left border
            self.dfs(board, i, c-1)  # right border

        for j in range(c):
            self.dfs(board, 0, j)  # top border
            self.dfs(board, r-1, j)  # bottom border

        # making 'O' into 'X' and '#' into 'O'
        for i in range(r):
            for j in range(c):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == '#':
                    board[i][j] = 'O'

    def dfs(self, board, i, j):
        if 0 <= i < len(board) and 0 <= j < len(board[0]) and board[i][j] == 'O':
            board[i][j] = '#'
            self.dfs(board, i+1, j)
            self.dfs(board, i-1, j)
            self.dfs(board, i, j+1)
            self.dfs(board, i, j-1)
