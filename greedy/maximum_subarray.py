class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        cur_sum = 0
        max_sum = float('-inf')
        for i in range(len(nums)):
            cur_sum += nums[i]
            cur_sum = max(cur_sum, nums[i])
            max_sum = max(max_sum, cur_sum)
        return max_sum


print(Solution().maxSubArray([2,-3,4,-2,2,1,-1,4])) #8
