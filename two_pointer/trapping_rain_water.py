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
        max_left = height[0]
        max_right = height[-1]
        left = cur = 0
        right = len(height) - 1

        while left < right:
            water += max(min(max_left, max_right) - height[cur], 0)
            if height[left] > max_left:
                max_left = height[left]
            elif height[right] > max_right:
                max_right = height[right]

            if max_left <= max_right:
                left += 1
                cur = left
            else:
                right -= 1
                cur = right

        return water

    def method(self):
        return self.trap

    def test_cases(self):
        return [
            ([0,1,0,2,1,0,1,3,2,1,2,1], 6),
            ([4,2,0,3,2,5], 9),
        ]

Solution().check()
