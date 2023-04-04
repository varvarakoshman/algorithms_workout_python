import unittest


# O(w * h) time | O(w * h) space, w - matrix's width, h - height
# Solution 1 (my initial) (modifying the input)
def riverSizes(matrix):
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
