# O(m*n) time | O(m*n) space
class Solution:
    def maxAreaOfIsland(self, grid):
        visited = set()
        max_size = 0

        def dfs(i, j):
            count = 0
            curr_pair = tuple([i, j])
            is_valid_pair = 0 <= i < len(grid) and 0 <= j < len(grid[0])
            if is_valid_pair and grid[i][j] == 1 and curr_pair not in visited:
                visited.add(curr_pair)
                count += 1
                count += dfs(i - 1, j)
                count += dfs(i, j - 1)
                count += dfs(i + 1, j)
                count += dfs(i, j + 1)
                return count
            else:
                return 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    continue
                curr_pair = tuple([i, j])
                if curr_pair not in visited:
                    max_size = max(max_size, dfs(i, j))
        return max_size


if __name__ == '__main__':
    solution = Solution()

    grid = [
        [1, 1, 1, 1, 0],
        [1, 1, 0, 1, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]
    assert solution.maxAreaOfIsland(grid) == 9

    grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
    assert solution.maxAreaOfIsland(grid) == 6

    grid = [[0, 0, 0, 0, 0, 0, 0, 0]]
    assert solution.maxAreaOfIsland(grid) == 0
