# https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: list[int]) -> int:
        max_area = 0
        l = 0
        r = len(height) - 1

        while l < r:
            w = r - l
            h = min(height[l], height[r])
            max_area = max(max_area, w * h)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return max_area

print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))