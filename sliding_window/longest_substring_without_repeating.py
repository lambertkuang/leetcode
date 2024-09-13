from util.test_case import TestCase

# https://leetcode.com/problems/longest-substring-without-repeating-characters/

"""
Given a string s, find the length of the longest substring without repeating characters.



Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""

class Solution(TestCase):
    def lengthOfLongestSubstring(self, s: str) -> int:
        # use a set to keep track of characters seen
        # keep track of two pointers, left and right starting from 0
        # increment right if current right char is not in set
        # keep track of current longest substring
        # increment left when right encounters an element in set, until
        # the duplicate element is removed from the set
        longest = 0
        left = right = 0
        seen = set()

        while right < len(s):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            longest = max(longest, len(seen))
            right += 1

        return longest

    def method(self):
        return self.lengthOfLongestSubstring

    def test_cases(self):
        return [
            ('abcabcbb', 3),
            ('bbbbb', 1),
            ('pwwkew', 3),
        ]

Solution().check()
