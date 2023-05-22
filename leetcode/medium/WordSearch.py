# O(m * n * 4^(len(word))) time | O(len(word)) space
class Solution:
    def exist(self, board, word):
        n_colons, n_rows = len(board[0]), len(board)
        path = set()

        def dfs(row, col, idx):
            if idx == len(word):
                return True

            curr_cell = tuple([row, col])
            if (row >= n_rows or col >= n_colons
                    or col < 0 or row < 0
                    or board[row][col] != word[idx]
                    or curr_cell in path):
                return False

            path.add(curr_cell)
            idx += 1
            is_found = dfs(row + 1, col, idx) or \
                       dfs(row - 1, col, idx) or \
                       dfs(row, col + 1, idx) or \
                       dfs(row, col - 1, idx)
            path.remove(curr_cell)
            return is_found

        for i in range(n_rows):
            for j in range(n_colons):
                if dfs(i, j, 0):
                    return True
        return False


if __name__ == '__main__':
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]

    word = "ABCCED"
    assert Solution().exist(board, word) is True

    word = "SEE"
    assert Solution().exist(board, word) is True

    word = "ABCB"
    assert Solution().exist(board, word) is False

    board = [["a", "a"]]
    word = "aaa"
    assert Solution().exist(board, word) is False

    board = [["A", "B", "C", "E"], ["S", "F", "E", "S"], ["A", "D", "E", "E"]]
    word = "ABCESEEEFS"
    assert Solution().exist(board, word) is True
