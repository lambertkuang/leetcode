from util.test_case import TestCase

"""
https://leetcode.com/problems/basic-calculator-ii/

Given a string s which represents an expression, evaluate this expression and return its value.

The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().



Example 1:

Input: s = "3+2*2"
Output: 7

Example 2:

Input: s = " 3/2 "
Output: 1

Example 3:

Input: s = " 3+5 / 2 "
Output: 5


Constraints:

1 <= s.length <= 3 * 105
s consists of integers and operators ('+', '-', '*', '/') separated by some number of spaces.
s represents a valid expression.
All the integers in the expression are non-negative integers in the range [0, 231 - 1].
The answer is guaranteed to fit in a 32-bit integer.
"""

class Solution(TestCase):
    def calculate(self, s: str) -> int:
        """
        1. Process string until number is found
        2. Push number onto stack
        3. If operator is * or /, pop from stack and evaluate expression with that of next number
        4. If operator is +, continue.
        5. If operator is -, multiply number by -1 and continue.
        """
        result = 0
        stack = []
        current: str = ''
        i = 0
        while i < len(s):
            c = s[i]
            if c.isnumeric():
                current += c
                i += 1
                continue

            if current:
                stack.append(int(current))
                current = ''
            if c == '*' or c == '/' or c == '-':
                # get the next value to evaluate expression
                next_n = ''
                i += 1
                while not next_n or (i < len(s) and s[i].isnumeric()):
                    if s[i].isnumeric():
                        next_n += s[i]
                    i += 1
                b = int(next_n)
                if c == '*':
                    a = stack.pop()
                    stack.append(a * b)
                elif c == '/':
                    a = stack.pop()
                    stack.append(int(a / b))
                elif c == '-':
                    stack.append(-1 * b)
                continue
            i += 1
        if current:
            stack.append(int(current))
        for v in stack:
            result += v
        return result

    def method(self):
        return self.calculate

    def test_cases(self):
        return [
            ("3+2*2", 7),
            (" 3/2 ", 1),
            (" 3+5 / 2 ", 5),
            ("1", 1),
            ("1-1-1", -1),
        ]


Solution().check()
