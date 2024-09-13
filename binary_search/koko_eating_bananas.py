import math
from util.test_case import TestCase


class Solution(TestCase):
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        # dependent on size of piles and number of hours given
        # max rate: largest pile size
        # min rate: num of piles
        # calculate num hours it would take at a certain rate
        left = 1
        right = max(piles)
        res = right
        while left <= right:
            speed = (left + right) // 2
            num_hours_taken = self.get_hours_at_speed(piles, speed)
            if num_hours_taken <= h:
                res = speed
                right = speed - 1
            elif num_hours_taken > h:
                left = speed + 1
        return res

    def get_hours_at_speed(self, piles: list[int], speed: int) -> int:
        total_hours = 0

        for pile in piles:
            total_hours += int(math.ceil(pile / speed))

        return total_hours

    def method(self):
        return self.minEatingSpeed

    def test_cases(self):
        return [
            ([1,4,3,2], 9, 2),
            ([25,10,23,4], 4, 25),
            ([312884470], 968709470, 1),
            ([1,1,1,999999999], 10, 142857143),
        ]


Solution().check()
