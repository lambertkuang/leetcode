from util.test_case import TestCase

# https://leetcode.com/problems/subsets-ii/
"""
Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
Example 2:

Input: nums = [0]
Output: [[],[0]]


Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
"""


class Solution(TestCase):
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        subsets = []
        nums.sort()

        def backtrack(cur: list, i: int):
            if i > len(nums):
                return

            subsets.append(cur.copy())
            prev = None
            for idx in range(i, len(nums)):
                if prev == nums[idx]:
                    continue
                cur.append(nums[idx])
                backtrack(cur, idx + 1)
                prev = cur.pop()

        backtrack([], 0)

        return subsets

    def method(self):
        return self.subsetsWithDup

    def test_cases(self):
        return [
            ([1,2,2], [[],[1],[1,2],[1,2,2],[2],[2,2]]),
        ]

Solution().run_tests()