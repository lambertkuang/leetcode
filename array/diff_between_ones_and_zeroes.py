from util.test_case import TestCase

# https://leetcode.com/problems/difference-between-ones-and-zeros-in-row-and-column/submissions/

"""
You are given a 0-indexed m x n binary matrix grid.

A 0-indexed m x n difference matrix diff is created with the following procedure:

Let the number of ones in the ith row be onesRowi.
Let the number of ones in the jth column be onesColj.
Let the number of zeros in the ith row be zerosRowi.
Let the number of zeros in the jth column be zerosColj.
diff[i][j] = onesRowi + onesColj - zerosRowi - zerosColj
Return the difference matrix diff.



Example 1:


Input: grid = [[0,1,1],[1,0,1],[0,0,1]]
Output: [[0,0,4],[0,0,4],[-2,-2,2]]
Explanation:
- diff[0][0] = onesRow0 + onesCol0 - zerosRow0 - zerosCol0 = 2 + 1 - 1 - 2 = 0
- diff[0][1] = onesRow0 + onesCol1 - zerosRow0 - zerosCol1 = 2 + 1 - 1 - 2 = 0
- diff[0][2] = onesRow0 + onesCol2 - zerosRow0 - zerosCol2 = 2 + 3 - 1 - 0 = 4
- diff[1][0] = onesRow1 + onesCol0 - zerosRow1 - zerosCol0 = 2 + 1 - 1 - 2 = 0
- diff[1][1] = onesRow1 + onesCol1 - zerosRow1 - zerosCol1 = 2 + 1 - 1 - 2 = 0
- diff[1][2] = onesRow1 + onesCol2 - zerosRow1 - zerosCol2 = 2 + 3 - 1 - 0 = 4
- diff[2][0] = onesRow2 + onesCol0 - zerosRow2 - zerosCol0 = 1 + 1 - 2 - 2 = -2
- diff[2][1] = onesRow2 + onesCol1 - zerosRow2 - zerosCol1 = 1 + 1 - 2 - 2 = -2
- diff[2][2] = onesRow2 + onesCol2 - zerosRow2 - zerosCol2 = 1 + 3 - 2 - 0 = 2
Example 2:


Input: grid = [[1,1,1],[1,1,1]]
Output: [[5,5,5],[5,5,5]]
Explanation:
- diff[0][0] = onesRow0 + onesCol0 - zerosRow0 - zerosCol0 = 3 + 2 - 0 - 0 = 5
- diff[0][1] = onesRow0 + onesCol1 - zerosRow0 - zerosCol1 = 3 + 2 - 0 - 0 = 5
- diff[0][2] = onesRow0 + onesCol2 - zerosRow0 - zerosCol2 = 3 + 2 - 0 - 0 = 5
- diff[1][0] = onesRow1 + onesCol0 - zerosRow1 - zerosCol0 = 3 + 2 - 0 - 0 = 5
- diff[1][1] = onesRow1 + onesCol1 - zerosRow1 - zerosCol1 = 3 + 2 - 0 - 0 = 5
- diff[1][2] = onesRow1 + onesCol2 - zerosRow1 - zerosCol2 = 3 + 2 - 0 - 0 = 5


Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 105
1 <= m * n <= 105
grid[i][j] is either 0 or 1.
"""

class Solution(TestCase):
    def onesMinusZeros(self, grid: list[list[int]]) -> list[list[int]]:
        count_ones_row = []
        count_zeroes_row = []
        count_ones_col = []
        count_zeroes_col = []
        diff = grid.copy()

        # fill in count ones/zeroes rows
        for row in grid:
            count_ones = 0
            count_zeroes = 0
            for val in row:
                if val == 1:
                    count_ones += 1
                elif val == 0:
                    count_zeroes += 1
            count_ones_row.append(count_ones)
            count_zeroes_row.append(count_zeroes)

        # fill in count ones/zeroes columns
        for j in range(len(grid[0])):
            count_ones = 0
            count_zeroes = 0
            for i in range(len(grid)):
                if grid[i][j] == 1:
                    count_ones += 1
                elif grid[i][j] == 0:
                    count_zeroes += 1
            count_ones_col.append(count_ones)
            count_zeroes_col.append(count_zeroes)

        # loop through grid and construct diff
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                diff[i][j] = count_ones_row[i] + count_ones_col[j] - count_zeroes_row[i] - count_zeroes_col[j]

        return diff

    def method(self):
        return self.onesMinusZeros

    def test_cases(self):
        return [
            ([[0,1,1],[1,0,1],[0,0,1]], [[0,0,4],[0,0,4],[-2,-2,2]]),
            ([[1,1,1],[1,1,1]], [[5,5,5],[5,5,5]]),
        ]

Solution().check()
