from typing import Optional
from util.list_node import ListNode

# https://leetcode.com/problems/reverse-linked-list/

"""
Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]

Example 3:
Input: head = []
Output: []
"""

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None

        while head:
            t = head.next
            head.next = prev
            prev = head
            head = t

        return prev