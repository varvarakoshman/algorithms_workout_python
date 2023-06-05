import unittest


# O(m*n) time | O(m*n) space
def transposeMatrix(matrix):
    n_rows, n_columns = len(matrix), len(matrix[0])
    result = [[0 for _ in range(n_rows)] for _ in range(n_columns)]
    for i in range(n_rows):
        for j in range(n_columns):
            result[j][i] = matrix[i][j]
    return result


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        expected = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
        actual = transposeMatrix(input)
        self.assertEqual(actual, expected)
