class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        results = set()
        nums.sort()
        prev = None
        length = len(nums)
        for i in range(length):
            if nums[i] == prev:
                continue

            l = i + 1
            r = length - 1
            while l < r:
                total = nums[l] + nums[r] + nums[i]
                if total == 0:
                    results.add((nums[l], nums[r], nums[i]))
                if total > 0:
                    r -= 1
                else:
                    l += 1
            prev = nums[i]

        norm = []
        for s in results:
            norm.append(list(s))
        return norm


print(Solution().threeSum([-1,0,1,2,-1,-4,-2,-3,3,0,4]))