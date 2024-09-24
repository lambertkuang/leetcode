from collections import deque

from util.test_case import TestCase

"""
https://leetcode.com/problems/word-search-ii/

Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.



Example 1:


Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]
Example 2:


Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []


Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 12
board[i][j] is a lowercase English letter.
1 <= words.length <= 3 * 104
1 <= words[i].length <= 10
words[i] consists of lowercase English letters.
All the strings of words are unique.
"""

class Node:
    def __init__(self) -> None:
        self.children = {}
        self.is_terminal = False


class Trie:
    def __init__(self) -> None:
        self.root = Node()

    def insert(self, word: str) -> None:
        cur = self.root
        for letter in word:
            if letter not in cur.children:
                cur.children[letter] = Node()
            cur = cur.children[letter]
        cur.is_terminal = True


class Solution(TestCase):
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        # construct trie
        trie = Trie()
        for word in words:
            trie.insert(word)

        # go through each element in board and find words
        rows = len(board)
        cols = len(board[0])
        found_words = set()
        visited = set()

        def backtrack(row: int, col: int, node: Node, cur: str):
            if node.is_terminal:
                found_words.add(cur)

            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for r, c in directions:
                nr = row + r
                nc = col + c
                if (
                    nr >= 0
                    and nr < len(board)
                    and nc >= 0
                    and nc < len(board[0])
                    and (nr, nc) not in visited
                    and board[nr][nc] in node.children
                ):
                    nl = board[nr][nc]
                    visited.add((nr, nc))
                    backtrack(nr, nc, node.children[nl], cur + nl)
                    visited.remove((nr, nc))

        for r in range(rows):
            for c in range(cols):
                letter = board[r][c]
                if letter in trie.root.children:
                    visited.add((r, c))
                    backtrack(r, c, trie.root.children[letter], letter)
                    visited.remove((r, c))

        return list(found_words)

    def method(self):
        return self.findWords

    def test_cases(self):
        return [
            ([["a","b","c","d"],["s","a","a","t"],["a","c","k","e"],["a","c","d","n"]], ["bat","cat","back","backend","stack"], ["back","backend","cat"]),
            ([["x","o"],["x","o"]], ["xoxo"], []),
            ([["o","a","b","n"],["o","t","a","e"],["a","h","k","r"],["a","f","l","v"]], ["oa","oaa"], ["oa","oaa"]),
            ([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], ["oath","pea","eat","rain","hklf","hf"], ["eat","hf","hklf","oath"]),
            ([["a","a"]], ["aaa"], []),
        ]

Solution().check()