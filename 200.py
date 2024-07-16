https://leetcode.com/problems/number-of-islands/description/
from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def markIsland(grid, r, c, x, y):
            q = deque([(x, y)])
            while q:
                (x, y) = q.popleft()
                grid[x][y] = "0"
                for i, j in ((x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)):
                    if 0 <= i < r and 0 <= j < c and grid[i][j] == "1":
                        q.append((i, j))
                        grid[i][j] = "0"

        r, c = len(grid), len(grid[0])
        islandCount = 0
        for x in range(r):
            for y in range(c):
                if grid[x][y] == "1":
                    islandCount += 1
                    markIsland(grid, r, c, x, y)

        return islandCount

