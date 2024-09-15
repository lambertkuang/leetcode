import heapq
from collections import defaultdict
from util.test_case import TestCase

# https://leetcode.com/problems/the-number-of-the-smallest-unoccupied-chair/

"""
There is a party where n friends numbered from 0 to n - 1 are attending. There is an infinite number of chairs in this party that are numbered from 0 to infinity. When a friend arrives at the party, they sit on the unoccupied chair with the smallest number.

For example, if chairs 0, 1, and 5 are occupied when a friend comes, they will sit on chair number 2.
When a friend leaves the party, their chair becomes unoccupied at the moment they leave. If another friend arrives at that same moment, they can sit in that chair.

You are given a 0-indexed 2D integer array times where times[i] = [arrivali, leavingi], indicating the arrival and leaving times of the ith friend respectively, and an integer targetFriend. All arrival times are distinct.

Return the chair number that the friend numbered targetFriend will sit on.



Example 1:

Input: times = [[1,4],[2,3],[4,6]], targetFriend = 1
Output: 1
Explanation:
- Friend 0 arrives at time 1 and sits on chair 0.
- Friend 1 arrives at time 2 and sits on chair 1.
- Friend 1 leaves at time 3 and chair 1 becomes empty.
- Friend 0 leaves at time 4 and chair 0 becomes empty.
- Friend 2 arrives at time 4 and sits on chair 0.
Since friend 1 sat on chair 1, we return 1.


Example 2:

Input: times = [[3,10],[1,5],[2,6]], targetFriend = 0
Output: 2
Explanation:
- Friend 1 arrives at time 1 and sits on chair 0.
- Friend 2 arrives at time 2 and sits on chair 1.
- Friend 0 arrives at time 3 and sits on chair 2.
- Friend 1 leaves at time 5 and chair 0 becomes empty.
- Friend 2 leaves at time 6 and chair 1 becomes empty.
- Friend 0 leaves at time 10 and chair 2 becomes empty.
Since friend 0 sat on chair 2, we return 2.


Constraints:

n == times.length
2 <= n <= 10^4
times[i].length == 2
1 <= arrivali < leavingi <= 10^5
0 <= targetFriend <= n - 1
Each arrivali time is distinct.
"""

class Solution(TestCase):
    def smallestChair(self, times: list[list[int]], targetFriend: int) -> int:
        # keep one heap for enter times, one heap for leave times
        chairs = [None] * len(times)
        next_empty_chair = 0
        enter = []
        leave = []
        for friend in range(len(times)):
            enter_time, leave_time = times[friend]
            heapq.heappush(enter, (enter_time, friend))
            heapq.heappush(leave, (leave_time, friend))

        # place friends in chairs, and remove them when they leave
        while enter or leave:
            if enter[0][0] < leave[0][0]:
                _, friend = heapq.heappop(enter)
                if friend == targetFriend:
                    return next_empty_chair
                chairs[next_empty_chair] = friend
                while chairs[next_empty_chair] is not None:
                    next_empty_chair += 1
            else:
                # process leaving friend
                _, friend = heapq.heappop(leave)
                i = chairs.index(friend)
                chairs[i] = None
                if i < next_empty_chair:
                    next_empty_chair = i

    def smallestChair2(self, times: list[list[int]], targetFriend: int) -> int:
        # all available chairs: 0 ... len(times) - 1
        available_chairs = list(range(len(times)))
        # leave_times will be a heap with items (leave_time, chair)
        leave_times = []
        for arrival, leave in sorted(times):
            # while the earliest leave time is less than or equal to arrival time,
            # we should update the available chairs by pushing the chair
            # back onto the available_chairs heap
            while leave_times and leave_times[0][0] <= arrival:
                heapq.heappush(available_chairs, heapq.heappop(leave_times)[1])

            # each arrival time is distinct, so we can identify targetFriend by their arrival time
            # once we find the target friend, we can just return the first available chair
            if arrival == times[targetFriend][0]:
                return available_chairs[0]

            # we can seat the current friend at the next available chair,
            # and update the leave_times
            heapq.heappush(leave_times, (leave, heapq.heappop(available_chairs)))

    def method(self):
        return self.smallestChair

    def test_cases(self):
        return [
            ([[1,4],[2,3],[4,6]], 1, 1),
            ([[3,10],[1,5],[2,6]], 0, 2),
            ([[65253,94097],[53112,69530],[81932,93953],[580,17372],[68060,71030],[89288,90296],[44959,88547],[6214,54011],[97818,99471],[78902,97146],[71212,82972],[59442,86960],[72154,86992],[53663,80857],[48804,48973],[21405,23283],[96683,97745],[44529,57089],[82381,95500],[77233,98954],[46567,78575],[61841,63803],[6965,8982],[73406,91256],[2908,44896],[13652,60043],[38007,70678],[39164,84350],[82783,83192],[12047,44261],[38040,95704],[91821,95627],[95954,96558],[42939,49574],[35645,85888],[88399,89499],[35336,95198],[29465,42867],[2901,59586],[27777,81800],[60421,76192],[24437,55571],[69910,91110],[19882,80672],[19066,61320],[56677,74370],[71594,84251],[38251,41916],[31467,66022],[76687,88548],[52754,91352],[10343,20946],[99927,99962],[45952,53275],[97823,98554],[48115,48895],[51322,66032],[69261,83519],[8709,58686],[43490,50560],[93228,98446],[16041,56850],[34634,68772],[15413,81430],[65434,79855],[37254,58101],[61815,89611],[49288,58728],[36730,99097]], 0, 5),
        ]


Solution().check()
