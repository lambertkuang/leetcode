from util.test_case import TestCase

# https://leetcode.com/problems/combination-sum-ii/

"""
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.



Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output:
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5
Output:
[
[1,2,2],
[5]
]


Constraints:

1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30
"""

class Solution(TestCase):
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        """
        Sort candidates so we can easily skip previously calculated values to avoid duplicates
        """
        candidates.sort()
        results = []

        def backtrack(cur, i):
            total = sum(cur)
            if total == target:
                results.append(cur.copy())
                return
            if i > len(candidates) or total > target:
                return

            prev = None
            for idx in range(i, len(candidates)):
                c = candidates[idx]
                if prev == c:
                    continue
                cur.append(c)
                backtrack(cur, idx + 1)
                prev = cur.pop()

        backtrack([], 0)
        return results

    def method(self):
        return self.combinationSum2

    def test_cases(self):
        return [
            ([10,1,2,7,6,1,5], 8, [[1,1,6],[1,2,5],[1,7],[2,6]]),
            ([2,5,2,1,2], 5, [[1,2,2],[5]]),
        ]

Solution().check()
