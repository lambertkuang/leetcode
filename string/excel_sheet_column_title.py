from util.test_case import TestCase

"""
https://leetcode.com/problems/excel-sheet-column-title/

Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28
...


Example 1:

Input: columnNumber = 1
Output: "A"
Example 2:

Input: columnNumber = 28
Output: "AB"
Example 3:

Input: columnNumber = 701
Output: "ZY"


Constraints:

1 <= columnNumber <= 231 - 1
"""

class Solution(TestCase):
    def convertToTitle(self, columnNumber: int) -> str:
        title = ''
        while columnNumber > 0:
            title = chr((columnNumber - 1) % 26 + 65) + title
            columnNumber = (columnNumber - 1) // 26
        return title

    def method(self):
        return self.convertToTitle

    def test_cases(self):
        return [
            (1, "A"),
            (26, "Z"),
            (28, "AB"),
            (52, "AZ"),
            (78, "BZ"),
            (701, "ZY"),
            (702, "ZZ"),
            (60458, "CKKH"),
            (6825682, "NXIDF"),
        ]

Solution().check()