from util.test_case import TestCase

# https://leetcode.com/problems/subsets/


class Solution(TestCase):
    def subsets(self, nums: list[int]) -> list[list[int]]:
        subsets = []

        def backtrack(i: int, cur: list):
            if i > len(nums):
                return

            subsets.append(cur.copy())
            for idx in range(i, len(nums)):
                cur.append(nums[idx])
                backtrack(idx + 1, cur)
                cur.pop()

        backtrack(0, [])

        return subsets

    def method(self):
        return self.subsets

    def test_cases(self):
        return [
            ([1,2,3], [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]),
        ]


Solution().check()
