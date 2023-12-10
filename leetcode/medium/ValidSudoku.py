from typing import (
    List,
)

# requires:
# time: visiting each element 1 time (9*9 elements in total)
# space: 27 sets (of size 9 at worst)
# class Solution(object):
#     def isValidSudoku(self, board):
#         rows = {i: set() for i in range(9)}
#         columns = {i: set() for i in range(9)}
#         squares = [[set() for _ in range(3)] for _ in range(3)]
#         for i in range(len(board)):
#             for j in range(len(board[0])):
#                 curr_elem = board[i][j]
#                 if curr_elem == '.':
#                     continue
#                 if not (self.is_valid(rows[i], curr_elem) and self.is_valid(columns[j], curr_elem)
#                         and self.is_valid(squares[int(i // 3)][int(j // 3)], curr_elem)):
#                     return False
#         return True
#
#     def is_valid(self, elements, curr_elem):
#         if curr_elem in elements:
#             return False
#         elements.add(curr_elem)
#         return True

# O(n^2) time | O(n^2) space
# O(1) | O(1) if we treat 9 as the only possible value
class Solution1:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        rows = {i: set() for i in range(n)}
        columns = {i: set() for i in range(n)}
        squares = [[set() for _ in range(3)] for _ in range(3)]

        for i in range(n):
            for j in range(n):
                curr_digit = board[i][j]
                if curr_digit == ".":
                    continue
                curr_row = rows[i]
                curr_column = columns[j]
                curr_square = squares[i // 3][j // 3]
                if self.check_is_valid(curr_row, curr_column, curr_square, curr_digit):
                    curr_row.add(curr_digit)
                    curr_column.add(curr_digit)
                    curr_square.add(curr_digit)
                else:
                    return False
        return True

    def check_is_valid(self, row, column, square, digit):
        return digit not in row and digit not in column and digit not in square


# O(n^2) time | O(3n) ~ O(n) space
# O(1) | O(1) if we treat 9 as the only possible value
class Solution2:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        rows = [0] * n
        columns = [0] * n
        squares = [0] * n

        for i in range(n):
            for j in range(n):
                curr_digit = board[i][j]
                if curr_digit == ".":
                    continue
                position = int(curr_digit) - 1

                if rows[i] & (1 << position):
                    return False
                rows[i] |= (1 << position)

                if columns[j] & (1 << position):
                    return False
                columns[j] |= (1 << position)

                square_idx = (i // 3) * 3 + j // 3
                if squares[square_idx] & (1 << position):
                    return False
                squares[square_idx] |= (1 << position)

        return True


if __name__ == '__main__':
    solutions = [Solution1(), Solution2()]
    for solution in solutions:
        assert solution.isValidSudoku([["5", "3", ".", ".", "7", ".", ".", ".", "."]
                                            , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
                                            , [".", "9", "8", ".", ".", ".", ".", "6", "."]
                                            , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
                                            , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
                                            , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
                                            , [".", "6", ".", ".", ".", ".", "2", "8", "."]
                                            , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
                                            , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]) is True

        assert solution.isValidSudoku([["8", "3", ".", ".", "7", ".", ".", ".", "."]
                                            , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
                                            , [".", "9", "8", ".", ".", ".", ".", "6", "."]
                                            , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
                                            , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
                                            , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
                                            , [".", "6", ".", ".", ".", ".", "2", "8", "."]
                                            , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
                                            , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]) is False
