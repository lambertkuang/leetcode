from util.test_case import TestCase

"""
https://leetcode.com/problems/search-in-rotated-sorted-array/submissions/

There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.



Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1


Constraints:

1 <= nums.length <= 5000
-104 <= nums[i] <= 104
All values of nums are unique.
nums is an ascending array that is possibly rotated.
-104 <= target <= 104
"""

class Solution(TestCase):
    def search(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]:
                # here the left portion of the array is sorted
                if nums[left] <= target and target <= nums[mid]:
                    # if the target is between the left and mid, we know that
                    # it has to be in the left portion of the array
                    # since we know that left <= mid
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                # and here the right portion of the array is sorted
                if target >= nums[mid] and target <= nums[right]:
                    # if the target is between mid and right, we know that
                    # it has to be in the right portion of the array
                    # since we already know mid <= right
                    left = mid + 1
                else:
                    right = mid - 1

        return -1

    def method(self):
        return self.search

    def test_cases(self):
        return [
            ([4,5,6,7,0,1,2], 0, 4),
            ([4,5,6,7,0,1,2], 3, -1),
            ([1], 0, -1),
            ([1,3], 3, 1),
            ([1,3], 1, 0),
            ([3,5,1], 3, 0),
            ([4,5,6,7,8,1,2,3], 8, 4),
            ([5,1,2,3,4], 1, 1),
        ]

Solution().check()
