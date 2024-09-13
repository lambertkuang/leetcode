from collections import deque
from util.test_case import TestCase

# https://leetcode.com/problems/number-of-islands/

class Solution(TestCase):
    def numIslands(self, grid: list[list[str]]) -> int:
        self.grid = grid
        rows = len(grid)
        cols = len(grid[0])
        self.visited = set()
        num_islands = 0

        for i in range(rows):
            for j in range(cols):
                cur = grid[i][j]
                if cur == '1' and (i, j) not in self.visited:
                    num_islands += 1
                    self.visited.add((i, j))
                    # bfs to find all connecting land
                    self.bfs((i, j))

        return num_islands

    def bfs(self, initial_location: tuple[int, int]):
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        queue = deque()
        queue.append(initial_location)
        while queue:
            for _ in range(len(queue)):
                # check each direction and mark visited
                loc = queue.popleft()
                for dir in directions:
                    nr = dir[0] + loc[0]
                    nc = dir[1] + loc[1]
                    if (nr in range(len(self.grid))
                        and nc in range(len(self.grid[0]))
                        and self.grid[nr][nc] == '1'
                        and (nr, nc) not in self.visited
                    ):
                        self.visited.add((nr, nc))
                        queue.append((nr, nc))


    def method(self):
        return self.numIslands

    def test_cases(self):
        return [
            (
                [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]], 1
            ),
            (
                [["0","1","0"],["1","0","1"],["0","1","0"]], 4
            )
        ]


Solution().check()