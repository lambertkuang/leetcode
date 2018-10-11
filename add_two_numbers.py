class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        You are given two non-empty linked lists representing two non-negative integers. The digits are
        stored in reverse order and each of their nodes contain a single digit. Add the two numbers and
        return it as a linked list.

        You may assume the two numbers do not contain any leading zero, except the number 0 itself.

        Example:

        Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
        Output: 7 -> 0 -> 8
        Explanation: 342 + 465 = 807.
        """
        head_node = None
        cur_node = None
        carry = 0
        while l1 is not None or l2 is not None or carry > 0:
            val1 = l1.val if l1 is not None else 0
            val2 = l2.val if l2 is not None else 0
            sum_val = val1 + val2 + carry
            if sum_val > 9:
                sum_val -= 10
                carry = 1
            else:
                carry = 0
            if head_node is None:
                cur_node = ListNode(sum_val)
                head_node = cur_node
            else:
                cur_node.next = ListNode(sum_val)
                cur_node = cur_node.next
            l1 = l1.next if l1 is not None else l1
            l2 = l2.next if l2 is not None else l2
        return head_node

