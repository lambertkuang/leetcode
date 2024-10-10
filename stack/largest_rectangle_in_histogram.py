from util.test_case import TestCase

"""
https://leetcode.com/problems/largest-rectangle-in-histogram/

Given an array of integers heights representing the histogram's bar height where the width of each bar is 1,
return the area of the largest rectangle in the histogram.


Example 1:


Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.


Example 2:


Input: heights = [2,4]
Output: 4


Constraints:

1 <= heights.length <= 105
0 <= heights[i] <= 104
"""

class Solution(TestCase):
    def largestRectangleArea(self, heights: list[int]) -> int:
        """
        Main idea is that only heights of equal or larger values
        can form rectangles across multiple indices. This allows us to use a
        stack to maintain potential rectangles of increasing heights.
        Once we encounter a height smaller than the previous height, we
        continuously pop from the stack until we reach a height smaller than
        the current, and calculate the largest rectangle value with each pop
        by using the difference in indices and the last popped height.
        Once we reach a value less than the current height, we can
        append the current height to the stack and continue.

        Time complexity: O(n)
        Space complexity: O(n)
        """
        largest = 0
        # items will be a tuple of (index, height)
        stack = []

        for i in range(len(heights)):
            cur = heights[i]
            last_i = i

            while stack and cur < stack[-1][1]:
                last_i, last_h = stack.pop()
                largest = max(largest, (i - last_i) * last_h)
            stack.append((last_i, cur))

        while stack:
            last_i, last_h = stack.pop()
            largest = max(largest, (len(heights) - last_i) * last_h)

        return largest

    def method(self):
        return self.largestRectangleArea

    def test_cases(self):
        return [
            ([2,1,5,6,2,3], 10),
            ([2,4], 4),
            ([7,1,7,2,2,4], 8),
            ([1,3,7], 7),
            ([0], 0),
        ]

Solution().check()
