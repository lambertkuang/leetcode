from util.test_case import TestCase

# https://leetcode.com/problems/maximum-subarray-sum-with-one-deletion/

# class Solution:
#     def maximumSum(self, arr: list[int]) -> int:
#         def find_max(arr: list[int]) -> int:
#             cur_sum = arr[0]
#             max_sum = cur_sum
#             sum_until_deletion = 0
#             deletion = None

#             for i in range(1, len(arr)):
#                 n = arr[i]
#                 cur_sum += n
#                 if n > cur_sum and (cur_sum <= 0 or cur_sum < max_sum or i == 1):
#                     cur_sum = n
#                     deletion = None
#                     sum_until_deletion = 0
#                 # print(cur_sum)
#                 if n < 0:
#                     if deletion is None:
#                         sum_until_deletion = cur_sum
#                         deletion = n
#                         if cur_sum != n:
#                             cur_sum -= deletion
#                     else:
#                         if n < deletion:
#                             if sum_until_deletion < 0:
#                                 cur_sum -= sum_until_deletion
#                                 sum_until_deletion = cur_sum
#                                 cur_sum += deletion
#                                 deletion = n
#                                 cur_sum -= deletion
#                             else:
#                                 cur_sum += deletion
#                                 cur_sum -= n
#                                 deletion = n


#                 if cur_sum < max_sum and cur_sum < 0 and n > 0:
#                     cur_sum = n
#                     deletion = None
#                     sum_until_deletion = 0
#                 max_sum = max(max_sum, cur_sum, n)
#             return max_sum
#         max_reversed = find_max(list(reversed(arr)))
#         # print('\n')
#         max_forward = find_max(arr)
#         return max(max_reversed, max_forward)


class Solution(TestCase):
    def maximumSum(self, arr: list[int]) -> int:
        # max_sum = float('-inf')
        # store = arr.copy()
        # max_store = arr.copy()

        # for i, n in reversed(list(enumerate(arr))):
        #     left = store[i + 2] if i + 2 < len(arr) else 0
        #     right = store[i + 1] if i + 1 < len(arr) else 0
        #     store[i] = max(n, right + n)
        #     right_max = max_store[i + 1] if i + 1 < len(arr) else 0
        #     max_store[i] = max(n, left + n, right_max + n)
        #     max_sum = max(max_sum, max_store[i])

        # return max_sum

        one_delete = 0
        no_delete = arr[0]
        max_sum = arr[0]

        for i in range(1, len(arr)):
            one_delete = max(one_delete + arr[i], no_delete)
            no_delete = max(no_delete + arr[i], arr[i])
            max_sum = max(max_sum, max(one_delete, no_delete))

        return max_sum

    def test_cases(self):
        return [
            ([1,-2,0,3], 4),
            ([1,-2,-2,3], 3),
            ([-1,-1,-1,-1], -1),
            ([5,-6,8,-4,2,1,3,-9,7], 17),
            ([1,-4,-5,-2,5,0,-1,2], 7),
            ([8,-1,6,-7,-4,5,-4,7,-6], 17),
            ([11,-10,-11,8,7,-6,9,4,11,6,5,0], 50),
            ([-16,-13,-26,5,-28,7,-10,-11,-28,15,-10,-27,12,-1,18,-15,28,-1,-18,9,-4,27,10,-11,-12,-1,18,-15,0,-17], 83),
            ([-17,10,-7,-4,11,-2,-11,8,-17,-14,17,-20,19,6,13,-8,7,-6,-7,12], 55),
            ([3,-4,-3,-8,3,-8,-11,4,-3,10,-1], 14),
            ([-50], -50),
            ([100,30,1,987,400,200,9], 1727),
            ([-7,-1], -1),
        ]

    def method(self):
        return self.maximumSum


Solution().run_tests()