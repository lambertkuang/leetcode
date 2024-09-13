from util.test_case import TestCase

# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution(TestCase):
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        cur_min = prices[0]

        for i in range(1, len(prices)):
            price = prices[i]
            if price < cur_min:
                cur_min = price
                continue

            max_profit = max(max_profit, price - cur_min)
        return max_profit

    def test_cases(self):
        return [
            ([7,1,5,3,6,4], 5),
            ([7,6,4,3,1], 0),
        ]

    def method(self):
        return self.maxProfit


Solution().check()
