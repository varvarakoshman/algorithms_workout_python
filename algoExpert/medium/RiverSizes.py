import unittest


# O(w * h) time | O(w * h) space, w - matrix's width, h - height
# Solution 1 (my initial) (modifying the input)
def riverSizes_0(matrix):
    river_sizes = []
    for row in range(len(matrix)):
        for column in range(len(matrix[0])):
            if matrix[row][column] == 1:
                river_sizes.append(dfs(row, column, matrix, 0))
    return river_sizes


def dfs(x, y, matrix, count):
    if x < 0 or y < 0 or y == len(matrix[0]) or x == len(matrix) or matrix[x][y] == 0:
        return 0
    matrix[x][y] = 0

    up = dfs(x - 1, y, matrix, count)
    down = dfs(x + 1, y, matrix, count)
    right = dfs(x, y + 1, matrix, count)
    left = dfs(x, y - 1, matrix, count)

    count += up
    count += down
    count += right
    count += left
    count += 1
    return count


# Solution 2 (iterative approach with no modifications to inout data)
# same time and space complexity
# O(w * h) time | O(w * h) space, w - matrix's width, h - height
def riverSizes(matrix):
    n_rows = len(matrix)
    n_columns = len(matrix[0])
    visited = [[False for _ in range(n_columns)] for _ in range(n_rows)]
    river_sizes = []
    for x in range(n_rows):
        for y in range(n_columns):
            if not visited[x][y] and matrix[x][y] == 1:
                river_sizes.append(find_river_size(x, y, matrix, visited))
    return river_sizes


def find_river_size(x, y, matrix, visited):
    curr_river_size = 0
    neighbours_stack = [[x, y]]
    while len(neighbours_stack) > 0:
        curr_node = neighbours_stack.pop()
        x = curr_node[0]
        y = curr_node[1]
        if visited[x][y]:
            continue
        if matrix[x][y] == 0:
            continue
        if x - 1 >= 0:
            neighbours_stack.append([x - 1, y])
        if x + 1 < len(matrix):
            neighbours_stack.append([x + 1, y])
        if y - 1 >= 0:
            neighbours_stack.append([x, y - 1])
        if y + 1 < len(matrix[0]):
            neighbours_stack.append([x, y + 1])
        curr_river_size += 1
        visited[x][y] = True
    return curr_river_size


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        testInput = [[1, 0, 0, 1, 0],
                     [1, 0, 1, 0, 0],
                     [0, 0, 1, 0, 1],
                     [1, 0, 1, 0, 1],
                     [1, 0, 1, 1, 0]]
        expected = [1, 2, 2, 2, 5]
        self.assertEqual(sorted(riverSizes(testInput)), expected)

        testInput = [[1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0],
                     [1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0],
                     [0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1],
                     [1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0],
                     [1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1]]
        expected = [2, 1, 21, 5, 2, 1]
        self.assertEqual(sorted(riverSizes(testInput)), sorted(expected))
