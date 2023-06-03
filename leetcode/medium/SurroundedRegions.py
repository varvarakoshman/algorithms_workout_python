# O(m*n) time | O(m*n) space
class Solution:
    def solve(self, board):
        self.traverse_diameter(board)
        self.capture(board, {'O': 'X', 'T': 'O'})

    def traverse_diameter(self, board):
        last_row, last_column = len(board) - 1, len(board[0]) - 1
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O' and (i in [0, last_row] or j in [0, last_column]):
                    self.dfs(board, i, j)

    def dfs(self, board, i, j):
        if not (0 <= i < len(board) and 0 <= j <= len(board[0]) - 1) or board[i][j] != 'O':
            return
        board[i][j] = 'T'
        self.dfs(board, i + 1, j)
        self.dfs(board, i - 1, j)
        self.dfs(board, i, j + 1)
        self.dfs(board, i, j - 1)

    def capture(self, board, replacements):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in replacements:
                    board[i][j] = replacements[board[i][j]]


if __name__ == '__main__':
    solution = Solution()

    board = [["X", "X", "X", "X"],
             ["X", "O", "O", "X"],
             ["X", "X", "O", "X"],
             ["X", "O", "X", "X"]]
    solution.solve(board)
    assert board == [["X", "X", "X", "X"],
                     ["X", "X", "X", "X"],
                     ["X", "X", "X", "X"],
                     ["X", "O", "X", "X"]]

    board = [["X"]]
    solution.solve(board)
    assert board == [["X"]]

    board = [["O", "X", "X", "O", "X"],
             ["X", "O", "O", "X", "O"],
             ["X", "O", "X", "O", "X"],
             ["O", "X", "O", "O", "O"],
             ["X", "X", "O", "X", "O"]]
    solution.solve(board)
    assert board == [["O", "X", "X", "O", "X"],
                     ["X", "X", "X", "X", "O"],
                     ["X", "X", "X", "O", "X"],
                     ["O", "X", "O", "O", "O"],
                     ["X", "X", "O", "X", "O"]]

    board = [["O", "O", "O", "O", "X", "X"],
             ["O", "O", "O", "O", "O", "O"],
             ["O", "X", "O", "X", "O", "O"],
             ["O", "X", "O", "O", "X", "O"],
             ["O", "X", "O", "X", "O", "O"],
             ["O", "X", "O", "O", "O", "O"]]
    solution.solve(board)
    assert board == [["O", "O", "O", "O", "X", "X"],
                     ["O", "O", "O", "O", "O", "O"],
                     ["O", "X", "O", "X", "O", "O"],
                     ["O", "X", "O", "O", "X", "O"],
                     ["O", "X", "O", "X", "O", "O"],
                     ["O", "X", "O", "O", "O", "O"]]
