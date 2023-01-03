# Solution 1 - iterative (initial)
# O(n) time | O(n) space
# n - total elements in the array
def spiralTraverse_1(array):
    if len(array) == 0:
        return array
    result = []
    iteration = 1
    n = len(array)
    m = len(array[0])
    max_iter_row = n // 2 + n % 2
    max_iter_col = m // 2 + m % 2
    while iteration <= max_iter_row and iteration <= max_iter_col:
        # traverse right
        curr_row = array[iteration - 1]
        for j in range(iteration - 1, m - iteration + 1):
            result.append(curr_row[j])
        # traverse down
        for i in range(iteration, n - iteration + 1):
            result.append(array[i][m - iteration])
        # traverse left
        curr_row = array[n - iteration]
        if iteration - 1 != n - iteration:
            for j in range(m - iteration - 1, iteration - 2, -1):
                result.append(curr_row[j])
        # traverse up
        if iteration - 1 != m - iteration:
            for i in range(n - iteration - 1, iteration - 1, -1):
                result.append(array[i][iteration - 1])
        iteration += 1
    return result


# Solution 1.2 (refactored)
# O(n) time | O(n) space
def spiralTraverse_2(array):
    if len(array) == 0:
        return array
    result = []
    start_col, end_col = 0, len(array[0]) - 1
    start_row, end_row = 0, len(array) - 1
    while start_col <= end_col and start_row <= end_row:
        # traverse right
        for j in range(start_col, end_col + 1):
            result.append(array[start_row][j])
        # traverse down
        for i in range(start_row + 1, end_row + 1):
            result.append(array[i][end_col])
        # traverse left
        if start_row != end_row:
            for j in range(end_col - 1, start_col - 1, -1):
                result.append(array[end_row][j])
        # traverse up
        if start_col != end_col:
            for i in range(end_row - 1, start_row, -1):
                result.append(array[i][start_col])
        start_col += 1
        start_row += 1
        end_col -= 1
        end_row -= 1
    return result


# Solution 2 - recursive
# O(n) time | O(n) space
def spiralTraverse(array):
    if len(array) == 0:
        return array
    result = []
    fill_result_with_traversal(array, result, 0, len(array[0]) - 1, 0, len(array) - 1)
    return result


def fill_result_with_traversal(array, result, start_col, end_col, start_row, end_row):
    if start_col <= end_col and start_row <= end_row:
        # traverse right
        for j in range(start_col, end_col + 1):
            result.append(array[start_row][j])
        # traverse down
        for i in range(start_row + 1, end_row + 1):
            result.append(array[i][end_col])
        # traverse left
        if start_row != end_row:
            for j in range(end_col - 1, start_col - 1, -1):
                result.append(array[end_row][j])
        # traverse up
        if start_col != end_col:
            for i in range(end_row - 1, start_row, -1):
                result.append(array[i][start_col])
        fill_result_with_traversal(array, result, start_col + 1, end_col - 1, start_row + 1, end_row - 1)


if __name__ == '__main__':
    assert spiralTraverse([[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]) == \
           [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    assert spiralTraverse([[1, 2, 3, 4], [8, 7, 6, 5]]) == [1, 2, 3, 4, 5, 6, 7, 8]
    assert spiralTraverse([[1, 2], [2, 3], [3, 4]]) == [1, 2, 3, 4, 3, 2]
    assert spiralTraverse([[1], [2], [3]]) == [1, 2, 3]
    assert spiralTraverse([[1, 2, 3]]) == [1, 2, 3]
    assert spiralTraverse([]) == []

# 1   2   3   4
# 12  13  14  5
# 11  16  15  6
# 10  9   8   7

