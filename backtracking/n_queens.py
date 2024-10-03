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

        def backtrack(row: int, cur: list[list[str]], remaining: int) -> None:
            if remaining + row > n or not self.isValidBoard(cur.copy()):
                return

            if remaining == 0 and self.isValidBoard(cur.copy()):
                solutions.append([''.join(r) for r in cur.copy()])
                return

            for r in range(row, n):
                for c in range(n):
                    cur[r][c] = 'Q'
                    backtrack(r + 1, cur, remaining - 1)
                    cur[r][c] = '.'

        backtrack(0, board, n)
        return solutions

    def isValidBoard(self, board: list[list[str]]) -> bool:
        # check that each row, col, and diagonal can have at most one queen
        n = len(board)
        # checking rows
        for row in board:
            has_queen = False
            for cell in row:
                if cell == 'Q':
                    if has_queen:
                        return False
                    has_queen = True

        # checking columns
        for c in range(n):
            has_queen = False
            for r in range(n):
                if board[r][c] == 'Q':
                    if has_queen:
                        return False
                    has_queen = True

        # checking diagonals
        for r in range(n):
            for c in range(n):
                left = self.checkLeftDiagonal(r, c, board)
                right = self.checkRightDiagonal(r, c, board)
                if not (left and right):
                    return False

        return True

    def checkLeftDiagonal(self, row: int, col: int, board: list[list[str]]) -> bool:
        has_queen = False
        while row < len(board) and col >= 0:
            if board[row][col] == 'Q':
                if has_queen:
                    return False
                has_queen = True
            row += 1
            col -= 1
        return True

    def checkRightDiagonal(self, row: int, col: int, board: list[list[str]]) -> bool:
        has_queen = False
        while row < len(board) and col < len(board):
            if board[row][col] == 'Q':
                if has_queen:
                    return False
                has_queen = True
            row += 1
            col += 1
        return True

    def method(self):
        return self.solveNQueens

    def test_cases(self):
        return [
            # (1, [["Q"]]),
            # (2, []),
            # (3, []),
            (4, [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]),
        ]

Solution().check()
