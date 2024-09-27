from collections import defaultdict

from util.test_case import TestCase

"""
https://leetcode.com/problems/top-k-frequent-elements/

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.



Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]


Constraints:

1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.


Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""

class Solution(TestCase):
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        top_k = []
        counts = defaultdict(int)
        # index will be count frequency, value will be a list of ints with that frequency
        buckets = [[] * i for i in range(len(nums) + 1)]
        for n in nums:
            counts[n] += 1
        for num, freq in counts.items():
            buckets[freq].append(num)
        for l in reversed(buckets):
            for n in l:
                top_k.append(n)
                if len(top_k) == k:
                    return top_k

    def method(self):
        return self.topKFrequent

    def test_cases(self):
        return [
            ([1,1,1,2,2,3], 2, [1,2]),
            ([1], 1, [1]),
        ]

Solution().check()
