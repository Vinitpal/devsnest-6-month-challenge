class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        count = 0
        row = len(grid)
        col = len(grid[0])

        for r in range(row):
            for c in range(col):
                if grid[r][c] == '1':
                    self.dfs(grid, r, c)
                    count += 1
        return count

    def dfs(self, grid, r, c):
        if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] != '1':
            return

        grid[r][c] = 'x'

        self.dfs(grid, r+1, c)
        self.dfs(grid, r-1, c)
        self.dfs(grid, r, c+1)
        self.dfs(grid, r, c-1)
