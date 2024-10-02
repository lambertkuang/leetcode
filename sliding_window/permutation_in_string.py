from collections import defaultdict

from util.test_case import TestCase

"""
https://leetcode.com/problems/permutation-in-string/

Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.



Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false


Constraints:

1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters.
"""

class Solution(TestCase):
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        # create count of s1
        s1count = defaultdict(int)
        for letter in s1:
            s1count[letter] += 1

        # sliding window and compare counts
        l = 0
        r = len(s1) - 1

        while r < len(s2):
            s2count = defaultdict(int)
            for i in range(l, r + 1):
                s2count[s2[i]] += 1
            if s1count == s2count:
                return True
            l += 1
            r += 1

        return False

    def method(self):
        return self.checkInclusion

    def test_cases(self):
        return [
            ('ab', 'eidbaooo', True),
            ('ab', 'eidboaoo', False),
            ('abcd', 'alksdfjkadbcaaldf', True),
            ('absdfjk', 'ae', False),
        ]

Solution().check()
