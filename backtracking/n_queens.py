from util.test_case import TestCase

"""
https://leetcode.com/problems/n-queens/

The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.



Example 1:


Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
Example 2:

Input: n = 1
Output: [["Q"]]


Constraints:

1 <= n <= 9
"""

class Solution(TestCase):
    def solveNQueens(self, n: int) -> list[list[str]]:
        solutions = []
        board = [['.' for _ in range(n)] for _ in range(n)]
        cols = set()
        pos_diagonal = set()
        neg_diagonal = set()

        def backtrack(row: int, cur: list[list[str]]) -> None:
            if row == n:
                solutions.append([''.join(r) for r in cur.copy()])
                return

            for col in range(n):
                if (
                    col in cols
                    or (row + col) in pos_diagonal
                    or (row - col) in neg_diagonal
                ):
                    continue
                cur[row][col] = 'Q'
                cols.add(col)
                pos_diagonal.add(row + col)
                neg_diagonal.add(row - col)

                backtrack(row + 1, cur)

                cur[row][col] = '.'
                cols.remove(col)
                pos_diagonal.remove(row + col)
                neg_diagonal.remove(row - col)

        backtrack(0, board)

        return solutions

    def method(self):
        return self.solveNQueens

    def test_cases(self):
        return [
            (1, [["Q"]]),
            (2, []),
            (3, []),
            (4, [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]),
        ]

Solution().check()
