from util.test_case import TestCase

"""
https://leetcode.com/problems/find-the-duplicate-number/

Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and using only constant extra space.



Example 1:

Input: nums = [1,3,4,2,2]
Output: 2
Example 2:

Input: nums = [3,1,3,4,2]
Output: 3
Example 3:

Input: nums = [3,3,3,3,3]
Output: 3


Constraints:

1 <= n <= 105
nums.length == n + 1
1 <= nums[i] <= n
All the integers in nums appear only once except for precisely one integer which appears two or more times.


Follow up:

How can we prove that at least one duplicate number must exist in nums?
Can you solve the problem in linear runtime complexity?
"""

class Solution(TestCase):
    def findDuplicate(self, nums: list[int]) -> int:
        # Floyd's cycle detection algorithm
        # https://en.wikipedia.org/wiki/Cycle_detection#Floyd's_tortoise_and_hare
        slow = nums[0]
        fast = nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        slow2 = 0
        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]
        return slow2

    def method(self):
        return self.findDuplicate

    def test_cases(self):
        return [
            ([3,1,3,4,2], 3),
            ([1,2,3,4,4], 4),
            ([1,2,3,2,2], 2),
        ]

Solution().check()