from util.test_case import TestCase

# https://leetcode.com/problems/word-search/

"""
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example 1:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

Example 2:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true

Example 3:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false


Constraints:

m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.


Follow up: Could you use search pruning to make your solution faster with a larger board?
"""

class Solution(TestCase):
    def exist(self, board: list[list[str]], word: str) -> bool:
        exists = False
        visited = set()
        def backtrack(r: int, c: int, word_idx: int):
            nonlocal exists
            if word[word_idx] == board[r][c] and word_idx == len(word) - 1:
                exists = True
                return

            directions = [[1, 0], [-1, 0], [0, -1], [0, 1]]
            for dir in directions:
                nr = r + dir[0]
                nc = c + dir[1]
                if (
                    nr >= 0
                    and nr < len(board)
                    and nc >= 0
                    and nc < len(board[0])
                    and (nr, nc) not in visited
                    and board[nr][nc] == word[word_idx + 1]
                ):
                    visited.add((nr, nc))
                    backtrack(nr, nc, word_idx + 1)
                    visited.remove((nr, nc))

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == word[0]:
                    visited.add((row, col))
                    backtrack(row, col, 0)
                    visited.remove((row, col))
                if exists == True:
                    return exists
        return exists

    def method(self):
        return self.exist

    def test_cases(self):
        return [
            ([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED", True),
            ([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE", True),
            ([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB", False),
            ([["a","a"]], "aaa", False),
        ]

Solution().run_tests()