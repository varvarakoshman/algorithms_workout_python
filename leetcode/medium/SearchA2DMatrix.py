# O(log(m) + log(n)) time | O(1) space
from typing import List


def searchMatrix(matrix, target):
    top_row, bottom_row = 0, len(matrix) - 1
    middle_idx = 0
    while top_row < bottom_row:
        middle_idx = (top_row + bottom_row) // 2
        smallest = matrix[middle_idx][0]
        largest = matrix[middle_idx][-1]
        if target > largest:
            top_row = middle_idx + 1
        elif target < smallest:
            bottom_row = middle_idx - 1
        elif largest == target or smallest == target:
            return True
        else:
            break
    if top_row == bottom_row:
        middle_idx = bottom_row
    return contains_with_bin_search(matrix[middle_idx], target)


def contains_with_bin_search(row, target):
    left, right = 0, len(row) - 1
    while left <= right:
        middle_idx = (left + right) // 2
        if row[middle_idx] > target:
            right = middle_idx - 1
        elif row[middle_idx] < target:
            left = middle_idx + 1
        else:
            return True
    return False


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m_rows = len(matrix)
        n_columns = len(matrix[0])
        right = m_rows * n_columns - 1
        left = 0
        while left <= right:
            middle = left + (right - left) // 2
            row = middle // n_columns
            column = middle % n_columns
            curr = matrix[row][column]
            if target > curr:
                left = middle + 1
            elif target < curr:
                right = middle - 1
            else:
                return True
        return False


if __name__ == '__main__':
    assert searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3) is True
    assert searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13) is False
    assert searchMatrix([[1, 3, 5], [10, 11, 16], [23, 30, 34]], 3) is True
    assert searchMatrix([[1, 3, 5], [10, 11, 16], [23, 30, 34]], 40) is False
    assert searchMatrix([[1, 3, 5]], 5) is True
    assert searchMatrix([[1], [3], [5]], 5) is True
    assert searchMatrix([[1]], 1) is True
    assert searchMatrix([[]], 1) is False
