# O(m*n) time | O(m*n) space
class Solution:
    def numIslands(self, grid):
        visited = set()
        island_count = 0

        def dfs(i, j):
            curr_pair = tuple([i, j])
            is_valid_pair = 0 <= i < len(grid) and 0 <= j < len(grid[0])
            if is_valid_pair and grid[i][j] == '1' and curr_pair not in visited:
                visited.add(curr_pair)
                dfs(i - 1, j)
                dfs(i, j - 1)
                dfs(i + 1, j)
                dfs(i, j + 1)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '0':
                    continue
                curr_pair = tuple([i, j])
                if curr_pair not in visited:
                    dfs(i, j)
                    island_count += 1
        return island_count


if __name__ == '__main__':
    solution = Solution()

    assert solution.numIslands([
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]) == 1

    assert solution.numIslands([
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]) == 3
