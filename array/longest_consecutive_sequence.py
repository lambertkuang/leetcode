from util.test_case import TestCase

"""
https://leetcode.com/problems/longest-consecutive-sequence/

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.



Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.


Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9


Constraints:

0 <= nums.length <= 105
-10^9 <= nums[i] <= 10^9
"""

class Solution(TestCase):
    def longestConsecutive(self, nums: list[int]) -> int:
        num_set = set(nums)
        longest = 0
        for n in num_set:
            cur = 0
            if n + 1 not in num_set:
                while n in num_set:
                    cur += 1
                    longest = max(longest, cur)
                    n -= 1
        return longest

    def method(self):
        return self.longestConsecutive

    def test_cases(self):
        return [
            ([100,4,200,1,3,2], 4),
            ([0,3,7,2,5,8,4,6,0,1], 9),
            ([123], 1),
        ]

Solution().check()
