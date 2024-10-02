from collections import defaultdict

from util.test_case import TestCase

# https://leetcode.com/problems/longest-repeating-character-replacement/

"""
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.


Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

Example 2:
Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.


Constraints:

1 <= s.length <= 105
s consists of only uppercase English letters.
0 <= k <= s.length
"""


class Solution(TestCase):
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        left = 0
        right = 0
        count = defaultdict(int)

        while right < len(s):
            c = s[right]
            count[c] += 1

            while (right - left + 1) - max(count.values()) > k:
                count[s[left]] -= 1
                left += 1

            longest = max(longest, right - left + 1)
            right += 1

        return longest

    def method(self):
        return self.characterReplacement

    def test_cases(self):
        return [
            ('ABAB', 2, 4),
            ('AABABBA', 1, 4),
            ('ABAA', 0, 2),
            ('ABCDEFGG', 2, 4),
            ('BBBBBE', 0, 5),
            ('AAAA', 2, 4),
            ('ABBB', 2, 4),
        ]

Solution().check()
