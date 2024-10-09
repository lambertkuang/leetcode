from util.test_case import TestCase


"""
https://leetcode.com/problems/trapping-rain-water/


Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it can trap after raining.


Example 1:

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
In this case, 6 units of rain water (blue section) are being trapped.


Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9


Constraints:

n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105
"""

class Solution(TestCase):
    def trap(self, height: list[int]) -> int:
        water = 0

        for i in range(1, len(height) - 1):
            max_left = max(height[0:i])
            max_right = max(height[i + 1:])
            cur = height[i]
            water += max(min(max_left, max_right) - cur, 0)

        return water

    def method(self):
        return self.trap

    def test_cases(self):
        return [
            ([0,1,0,2,1,0,1,3,2,1,2,1], 6),
            ([4,2,0,3,2,5], 9),
        ]

Solution().check()
