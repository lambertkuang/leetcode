from copy import deepcopy
from collections import deque

from util.test_case import TestCase

# https://leetcode.com/problems/rotting-oranges/

"""
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.



Example 1:
Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

Example 2:
Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

Example 3:
Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.


Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 10
grid[i][j] is 0, 1, or 2.
"""


class Solution(TestCase):
    def orangesRotting(self, grid: list[list[int]]) -> int:
        # go through each element in grid
        # find min distance to rotting orange from fresh oranges
        # return -1 if not possible
        self.grid = grid
        self.time_grid = deepcopy(self.grid)
        self.visited_grid = set()
        rows = len(grid)
        cols = len(grid[0])
        max_time_to_rot = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    self.fill_time_grid(r, c)
                # if grid[r][c] == 1:
                #     time_to_rot = self.get_time_to_rot(r, c)
                #     if time_to_rot == -1:
                #         return -1
                #     max_time_to_rot = max(max_time_to_rot, time_to_rot)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in self.visited_grid:
                    return -1
                if (r, c) in self.visited_grid:
                    max_time_to_rot = max(max_time_to_rot, self.time_grid[r][c])

        return max_time_to_rot

    def fill_time_grid(self, r: int, c: int) -> None:
        visited = set()
        q = deque()
        q.append((r, c))
        directions = [[1, 0], [-1, 0], [0, -1], [0, 1]]
        time_taken = 0
        while q:
            for _ in range(len(q)):
                row, col = q.popleft()
                visited.add((row, col))
                for dir in directions:
                    nr = row + dir[0]
                    nc = col + dir[1]
                    if (
                        nr >= 0
                        and nr < len(self.grid)
                        and nc >= 0
                        and nc < len(self.grid[0])
                        and (nr, nc) not in visited
                        and self.grid[nr][nc] == 1
                    ):
                        if (nr, nc) in self.visited_grid:
                            self.time_grid[nr][nc] = min(self.time_grid[nr][nc], time_taken + 1)
                        else:
                            self.time_grid[nr][nc] = time_taken + 1
                        self.visited_grid.add((nr, nc))
                        q.append((nr, nc))
            time_taken += 1


    def get_time_to_rot(self, r: int, c: int) -> int:
        visited = set()
        q = deque()
        q.append((r, c))
        time = 0
        directions = [[1, 0], [-1, 0], [0, -1], [0, 1]]
        while q:
            for _ in range(len(q)):
                row, col = q.popleft()
                for dir in directions:
                    nr = row + dir[0]
                    nc = col + dir[1]
                    is_in_range = (
                        nr >= 0
                        and nr < len(self.grid)
                        and nc >= 0
                        and nc < len(self.grid[0])
                    )
                    if (
                        is_in_range
                        and (nr, nc) not in visited
                        and self.grid[nr][nc] == 1
                    ):
                        q.append((nr, nc))
                    elif is_in_range and self.grid[nr][nc] == 2:
                        return time + 1
            time += 1
        return -1

    def method(self):
        return self.orangesRotting

    def test_cases(self):
        return [
            ([[2,1,1],[1,1,0],[0,1,1]], 4),
            ([[2,1,1],[0,1,1],[1,0,1]], -1),
            ([[0,2]], 0),
        ]

Solution().run_tests()