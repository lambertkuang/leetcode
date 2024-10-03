from util.test_case import TestCase

"""
https://leetcode.com/problems/permutations-ii/

Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.



Example 1:

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]
Example 2:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]


Constraints:

1 <= nums.length <= 8
-10 <= nums[i] <= 10
"""

class Solution(TestCase):
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        permutations = []
        nums.sort()
        def backtrack(cur: list, remaining: list) -> None:
            if len(cur) == len(nums):
                permutations.append(cur.copy())
                return

            prev = None
            for i in range(len(remaining)):
                if remaining[i] == prev:
                    continue
                cur.append(remaining[i])
                backtrack(cur, remaining[0:i] + remaining[i + 1:])
                cur.pop()
                prev = remaining[i]

        backtrack([], nums)

        return permutations

    def method(self):
        return self.permuteUnique

    def test_cases(self):
        return [
            ([1,1,2], [[1,1,2],[1,2,1],[2,1,1]]),
            ([1,2,3], [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]),
            ([6,10,9,8], [[6,8,9,10],[6,8,10,9],[6,9,8,10],[6,9,10,8],[6,10,8,9],[6,10,9,8],[8,6,9,10],[8,6,10,9],[8,9,6,10],[8,9,10,6],[8,10,6,9],[8,10,9,6],[9,6,8,10],[9,6,10,8],[9,8,6,10],[9,8,10,6],[9,10,6,8],[9,10,8,6],[10,6,8,9],[10,6,9,8],[10,8,6,9],[10,8,9,6],[10,9,6,8],[10,9,8,6]]),
        ]

Solution().check()
