from util.test_case import TestCase

# https://leetcode.com/problems/max-area-of-island/


class Solution(TestCase):
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        max_area = 0
        rows = len(grid)
        cols = len(grid[0])
        visited = set()

        def dfs(row, col) -> int:
            nonlocal rows
            nonlocal cols
            nonlocal grid
            nonlocal visited

            if (
                row not in range(rows)
                or col not in range(cols)
                or grid[row][col] != 1
                or (row, col) in visited
            ):
                return 0

            visited.add((row, col))
            area = 1

            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dir in directions:
                area += dfs(dir[0] + row, dir[1] + col)
            return area


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    max_area = max(max_area, dfs(r, c))

        return max_area

    def method(self):
        return self.maxAreaOfIsland

    def test_cases(self):
        return [
            (
                [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]], 6
            ),
        ]


Solution().check()