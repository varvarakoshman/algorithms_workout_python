# transpose matrix and then reverse the order of its columns
# O(n^2) time | O(1) space
class Solution:
    def rotate(self, matrix):
        size = len(matrix)
        self.transpose_in_place(matrix)
        for i in range(size):
            for j in range(size // 2):
                matrix[i][j], matrix[i][size - 1 - j] = matrix[i][size - 1 - j], matrix[i][j]
        return matrix

    def transpose_in_place(self, matrix):
        size = len(matrix)
        for i in range(size):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


if __name__ == '__main__':
    solution = Solution()
    assert solution.rotate([[1, 2, 3],
                            [4, 5, 6],
                            [7, 8, 9]]) == [[7, 4, 1],
                                            [8, 5, 2],
                                            [9, 6, 3]]
    assert solution.rotate([[5, 1, 9, 11],
                            [2, 4, 8, 10],
                            [13, 3, 6, 7],
                            [15, 14, 12, 16]]) == [[15, 13, 2, 5],
                                                   [14, 3, 4, 1],
                                                   [12, 6, 8, 9],
                                                   [16, 7, 10, 11]]

    assert solution.rotate([[1, 2],
                           [3, 4]]) == [[3, 1],
                                        [4, 2]]

    assert solution.rotate([[1]]) == [[1]]
