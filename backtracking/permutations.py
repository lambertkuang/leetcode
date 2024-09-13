from util.test_case import TestCase

# https://leetcode.com/problems/permutations/

class Solution(TestCase):
    def permute(self, nums: list[int]) -> list[list[int]]:
        permutations = []

        def backtrack(cur: list, remaining: list) -> None:
            if not remaining:
                permutations.append(cur.copy())
                return

            for i in range(len(remaining)):
                cur.append(remaining[i])
                backtrack(cur, remaining[0:i] + remaining[i + 1:])
                cur.pop()

        backtrack([], nums)
        return permutations

    def method(self):
        return self.permute

    def test_cases(self):
        return [
            ([1,2,3], [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]),
        ]


Solution().check()