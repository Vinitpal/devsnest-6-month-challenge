def get_area(grid, non_vis, src, dirs):
    ans = 1
    si, sj = src
    for i, j in dirs:
        newi, newj = si + i, sj + j
        if (newi, newj) in non_vis:
            non_vis.remove((newi, newj))
            ans += get_area(grid, non_vis, (newi, newj), dirs)
    return ans


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        non_vis = set()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    non_vis.add((i, j))

        max_area = 0
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while len(non_vis):
            max_area = max(max_area, get_area(
                grid, non_vis, non_vis.pop(), dirs))
        return max_area
