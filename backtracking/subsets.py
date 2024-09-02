from util.test_case import TestCase

# https://leetcode.com/problems/subsets/


class Solution(TestCase):
    def subsets(self, nums: list[int]) -> list[list[int]]:
        results = []

        def backtrack(r, i):
            nonlocal nums
            nonlocal results
            if i > len(nums):
                return
            results.append(r.copy())
            for n in range(i, len(nums)):
                r.append(nums[n])
                backtrack(r, n + 1)
                r.pop()

        backtrack([], 0)
        return results

    def method(self):
        return self.subsets

    def test_cases(self):
        return [
            ([1,2,3], [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]),
        ]


Solution().run_tests()
