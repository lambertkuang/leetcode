from util.test_case import TestCase

"""
https://leetcode.com/problems/product-of-array-except-self/

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.



Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]


Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.


Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
"""

class Solution(TestCase):
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        solution = []
        product = 1
        for n in nums:
            product *= n
            solution.append(product)

        product = 1
        for i in range(len(solution) - 1, -1, -1):
            if i - 1 >= 0:
                solution[i] = solution[i - 1] * product
            else:
                solution[i] = product
            product *= nums[i]

        return solution

    def method(self):
        return self.productExceptSelf

    def test_cases(self):
        return [
            ([1,2,3,4], [24,12,8,6]),
            ([-1,1,0,-3,3], [0,0,9,0,0]),
            ([-1,0,1,2,3], [0,-6,0,0,0]),
        ]

Solution().check()
