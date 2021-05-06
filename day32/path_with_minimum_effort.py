class Solution:
    def minimumEffortPath(self, heights):
        row, col = len(heights), len(heights[0])
        dist = [[-1]*col for i in range(row)]

        # effort #r #c #w
        heap = [(0, (0, 0, heights[0][0]))]

        while heap:
            newdiff, (r, c, w) = heappop(heap)

            if not 0 <= r < row or not 0 <= c < col:
                continue
            newdiff = max(newdiff, abs(w-heights[r][c]))

            if dist[r][c] == -1 or newdiff < dist[r][c]:
                dist[r][c] = newdiff
            else:
                continue
            heappush(heap, (newdiff, (r, c+1, heights[r][c])))
            heappush(heap, (newdiff, (r, c-1, heights[r][c])))
            heappush(heap, (newdiff, (r+1, c, heights[r][c])))
            heappush(heap, (newdiff, (r-1, c, heights[r][c])))
        return dist[row-1][col-1]
