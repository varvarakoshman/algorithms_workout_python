# Solution 1
# O(n*logm) time | O(1) space
def searchInSortedMatrix_1(matrix, target):
    for i in range(len(matrix)):
        row = matrix[i]
        match_idx = binary_search(row, target)
        if match_idx != -1:
            return [i, match_idx]
    return [-1, -1]


def binary_search(array, target):
    left = 0
    right = len(array) - 1
    while left <= right:
        middle = (left + right) // 2
        potential_match = array[middle]
        if target == potential_match:
            return middle
        if target > potential_match:
            left = middle + 1
        else:
            right = middle - 1
    return -1


# Solution 2
# O(n + m) time | O(1) space, n - # of rows, m - # of columns
def search_in_sorted_matrix(matrix, target):
    row = 0
    col = len(matrix[0]) - 1
    while row < len(matrix) and col >= 0:
        if matrix[row][col] > target:
            col -= 1
        elif matrix[row][col] < target:
            row += 1
        else:
            return [row, col]
    return [-1, -1]


if __name__ == '__main__':
    assert search_in_sorted_matrix([
        [1, 4, 7, 12, 15, 1000],
        [2, 5, 19, 31, 32, 1001],
        [3, 8, 24, 33, 35, 1002],
        [40, 41, 42, 44, 45, 1003],
        [99, 100, 103, 106, 128, 1004]
    ], 44) == [3, 3]  # in the middle
    assert search_in_sorted_matrix([
        [1, 4, 7, 12, 15, 1000],
        [2, 5, 19, 30, 32, 1001],
        [3, 8, 24, 33, 35, 1002],
        [40, 41, 42, 44, 45, 1003],
        [99, 100, 103, 106, 128, 1004]
    ], 33) == [2, 3]  # in the middle
    assert search_in_sorted_matrix([
        [1, 4, 7, 12, 15, 1000],
        [2, 5, 19, 31, 32, 1001],
        [3, 8, 24, 33, 35, 1002],
        [40, 41, 42, 44, 45, 1003],
        [99, 100, 103, 106, 128, 1004]
    ], 1) == [0, 0]  # top left
    assert search_in_sorted_matrix([
        [1, 4, 7, 12, 15, 1000],
        [2, 5, 19, 31, 32, 1001],
        [3, 8, 24, 33, 35, 1002],
        [40, 41, 42, 44, 45, 1003],
        [99, 100, 103, 106, 128, 1004]
    ], 1000) == [0, 5]  # top right
    assert search_in_sorted_matrix([
        [1, 4, 7, 12, 15, 1000],
        [2, 5, 19, 31, 32, 1001],
        [3, 8, 24, 33, 35, 1002],
        [40, 41, 42, 44, 45, 1003],
        [99, 100, 103, 106, 128, 1004]
    ], 1004) == [4, 5]  # top right
