class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        # binary search rows
        # identify row, binary search selected row
        l = 0
        r = len(matrix) - 1

        while l <= r:
            # get middle row and see if target fits
            m = (l + r) // 2
            row = matrix[m]
            if target >= row[0] and target <= row[-1]:
                # do another binary search on this row
                left = 0
                right = len(row) - 1
                while left < right:
                    middle = (left + right) // 2
                    if row[middle] == target:
                        return True
                    if row[middle] > target:
                        right = middle - 1
                    elif row[middle] < target:
                        left = middle + 1
                return False
            elif target < row[0]:
                r = m - 1
            elif target > row[-1]:
                l = m + 1

        return False


test_cases = [
    ([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3, True),
    ([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13, False),
]

for t1, t2, expected in test_cases:
    actual = Solution().searchMatrix(t1, t2)
    try:
        assert actual == expected
    except AssertionError:
        print('\033[91m' + f"Testcase failed: {t1}")
        print('\033[91m' + f"Expected: {expected} Actual: {actual}")
