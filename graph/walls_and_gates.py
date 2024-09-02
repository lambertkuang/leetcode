from collections import deque
from util.test_case import TestCase

# https://www.lintcode.com/problem/663/

class Solution(TestCase):
    def islandsAndTreasure(self, grid: list[list[int]]) -> None:
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 0:
                    self.bfs(grid, row, col)

    def bfs(self, grid, row, col):
        # return the distance to the nearest treasure
        distance = 0
        visited = set()
        queue = deque()
        queue.append((row, col))
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                visited.add((r, c))
                for dir in directions:
                    nr = dir[0] + r
                    nc = dir[1] + c
                    if (
                        nr in range(len(grid))
                        and nc in range(len(grid[0]))
                        and grid[nr][nc] > 0
                        and (nr, nc) not in visited
                    ):
                        if grid[nr][nc] < distance + 1:
                            continue
                        grid[nr][nc] = distance + 1
                        queue.append((nr, nc))
            distance += 1

    def method(self):
        return self.islandsAndTreasure

    def test_cases(self):
        return [
            (
                [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]], [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]
            ),
        ]