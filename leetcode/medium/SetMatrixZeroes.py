# O(m * n) time | O(n+ m) space
class Solution1:
    def setZeroes(self, matrix):
        N_ROWS, N_COLUMNS = len(matrix), len(matrix[0])

        zero_columns, zero_rows = set(), set()
        for i in range(N_ROWS):
            for j in range(N_COLUMNS):
                if matrix[i][j] == 0:
                    zero_rows.add(i)
                    zero_columns.add(j)
        for i in range(N_ROWS):
            for j in range(N_COLUMNS):
                if i in zero_rows or j in zero_columns:
                    matrix[i][j] = 0


# O(m * n) time | O(1) space
class Solution2:
    def setZeroes(self, matrix):
        N_ROWS, N_COLUMNS = len(matrix), len(matrix[0])
        row_zero = False

        for i in range(N_ROWS):
            for j in range(N_COLUMNS):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    if i > 0:
                        matrix[i][0] = 0
                    else:
                        row_zero = True

        for i in range(1, N_ROWS):
            for j in range(1, N_COLUMNS):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if matrix[0][0] == 0:
            for i in range(N_ROWS):
                matrix[i][0] = 0
        if row_zero:
            for j in range(N_COLUMNS):
                matrix[0][j] = 0


if __name__ == '__main__':
    solutions = [Solution1(), Solution2()]
    for solution in solutions:
        matrix = [[1, 1, 1],
                  [1, 0, 1],
                  [1, 1, 1]]
        solution.setZeroes(matrix)
        assert matrix == [[1, 0, 1],
                          [0, 0, 0],
                          [1, 0, 1]]

    for solution in solutions:
        matrix = [[0, 1, 2, 0],
                  [3, 4, 5, 2],
                  [1, 3, 1, 5]]
        solution.setZeroes(matrix)
        assert matrix == [[0, 0, 0, 0],
                          [0, 4, 5, 0],
                          [0, 3, 1, 0]]

    for solution in solutions:
        matrix = [[1, 2, 3, 0, 9]]
        solution.setZeroes(matrix)
        assert matrix == [[0, 0, 0, 0, 0]]

    for solution in solutions:
        matrix = [[1, 2, 3, 2, 9]]
        solution.setZeroes(matrix)
        assert matrix == [[1, 2, 3, 2, 9]]

    for solution in solutions:
        matrix = [[1], [2], [3], [0], [9]]
        solution.setZeroes(matrix)
        assert matrix == [[0], [0], [0], [0], [0]]
