# requires:
# time: visiting each element 1 time (9*9 elements in total)
# space: 27 sets (of size 9 at worst)
class Solution(object):
    def isValidSudoku(self, board):
        rows = {i: set() for i in range(9)}
        columns = {i: set() for i in range(9)}
        squares = [[set() for _ in range(3)] for _ in range(3)]
        for i in range(len(board)):
            for j in range(len(board[0])):
                curr_elem = board[i][j]
                if curr_elem == '.':
                    continue
                if not (self.is_valid(rows[i], curr_elem) and self.is_valid(columns[j], curr_elem)
                        and self.is_valid(squares[int(i // 3)][int(j // 3)], curr_elem)):
                    return False
        return True

    def is_valid(self, elements, curr_elem):
        if curr_elem in elements:
            return False
        elements.add(curr_elem)
        return True


if __name__ == '__main__':
    assert Solution().isValidSudoku([["5", "3", ".", ".", "7", ".", ".", ".", "."]
                                        , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
                                        , [".", "9", "8", ".", ".", ".", ".", "6", "."]
                                        , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
                                        , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
                                        , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
                                        , [".", "6", ".", ".", ".", ".", "2", "8", "."]
                                        , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
                                        , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]) is True

    assert Solution().isValidSudoku([["8", "3", ".", ".", "7", ".", ".", ".", "."]
                                        , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
                                        , [".", "9", "8", ".", ".", ".", ".", "6", "."]
                                        , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
                                        , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
                                        , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
                                        , [".", "6", ".", ".", ".", ".", "2", "8", "."]
                                        , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
                                        , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]) is False
