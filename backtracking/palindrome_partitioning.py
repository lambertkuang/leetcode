from util.test_case import TestCase

# https://leetcode.com/problems/palindrome-partitioning/

"""
Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]

Example 2:

Input: s = "a"
Output: [["a"]]


Constraints:

1 <= s.length <= 16
s contains only lowercase English letters.
"""

class Solution(TestCase):
    def partition(self, s: str) -> list[list[str]]:
        partitions = []

        def backtrack():
            pass

        return partitions

    def is_palindrome(s: str) -> bool:
        l = len(s)
        for i in range(l):
            if s[i] != s[l - i - 1]:
                return False
        return True

    def method(self):
        return self.partition

    def test_cases(self):
        return [
            ('aab', [["a","a","b"],["aa","b"]]),
            ('a', [["a"]]),
        ]


Solution().run_tests()