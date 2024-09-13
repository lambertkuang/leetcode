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
        # start from all rotten oranges
        # enqueue all rotten oranges, BFS from there
        q = deque()
        visited = set()
        directions = [[1, 0], [-1, 0], [0, -1], [0, 1]]
        total_fresh = 0
        time_taken = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    total_fresh += 1
                if grid[row][col] == 2:
                    q.append((row, col))

        while q:
            print(q)
            for _ in range(len(q)):
                row, col = q.popleft()
                for dir in directions:
                    nr = row + dir[0]
                    nc = col + dir[1]
                    if (
                        nr >= 0
                        and nr < len(grid)
                        and nc >= 0
                        and nc < len(grid[0])
                        and (nr, nc) not in visited
                        and grid[nr][nc] == 1
                    ):
                        visited.add((nr, nc))
                        total_fresh -= 1
                        q.append((nr, nc))
            time_taken += 1
        if total_fresh > 0:
            return -1
        return max(time_taken - 1, 0)

    def method(self):
        return self.orangesRotting

    def test_cases(self):
        return [
            ([[2,1,1],[1,1,0],[0,1,1]], 4),
            ([[2,1,1],[0,1,1],[1,0,1]], -1),
            ([[0,2]], 0),
            ([[2,1,1],[0,1,1],[1,0,1]], -1),
            ([[0]], 0),
            ([[2,2],[1,1],[0,0],[2,0]], 1),
        ]

Solution().check()