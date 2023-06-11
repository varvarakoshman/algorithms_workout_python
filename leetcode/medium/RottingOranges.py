# O(m*n) time | O(m*n) space
class Solution:
    def orangesRotting(self, grid):
        N_ROWS, N_COLS = len(grid), len(grid[0])
        visited = set()

        def bfs(nodes_queue):
            curr_minutes = 0
            visited.update(nodes_queue)
            while len(nodes_queue) > 0:
                n_nodes_per_pass = len(nodes_queue)
                new_nodes_to_add = set()
                for count in range(n_nodes_per_pass):
                    top_node = nodes_queue.pop(0)
                    visited.add(top_node)
                    curr_neighbours = get_unvisited_neighbours(top_node)
                    for curr_neighbour in curr_neighbours:
                        new_nodes_to_add.add(curr_neighbour)
                if len(new_nodes_to_add) > 0:
                    nodes_queue.extend(new_nodes_to_add)
                    visited.update(new_nodes_to_add)
                    curr_minutes += 1
            return curr_minutes

        def get_unvisited_neighbours(curr):
            curr_i, curr_j = curr
            curr_neighbours = [tuple([curr_i - 1, curr_j]),
                               tuple([curr_i + 1, curr_j]),
                               tuple([curr_i, curr_j - 1]),
                               tuple([curr_i, curr_j + 1])]
            valid_neighbours = []
            for neighbour in curr_neighbours:
                new_i, new_j = neighbour
                if neighbour not in visited and 0 <= new_i < N_ROWS and 0 <= new_j < N_COLS and grid[new_i][new_j] == 1:
                    valid_neighbours.append(neighbour)
            return valid_neighbours

        def check_if_all_rotting():
            is_all_rotting = True
            for row in range(N_ROWS):
                for col in range(N_COLS):
                    if grid[row][col] == 1:
                        is_all_rotting = is_all_rotting and tuple([row, col]) in visited
            return is_all_rotting

        starting_nodes = []
        for i in range(N_ROWS):
            for j in range(N_COLS):
                if grid[i][j] == 2:
                    starting_nodes.append(tuple([i, j]))
        n_minutes = bfs(starting_nodes)
        return n_minutes if check_if_all_rotting() else -1


if __name__ == '__main__':
    solution = Solution()
    grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    assert solution.orangesRotting(grid) == 4

    grid = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
    assert solution.orangesRotting(grid) == -1

    grid = [[0, 2]]
    assert solution.orangesRotting(grid) == 0

    grid = [[2, 1, 1], [1, 1, 1], [0, 1, 2]]
    assert solution.orangesRotting(grid) == 2

    grid = [[2, 2], [1, 1], [0, 0], [2, 0]]
    assert solution.orangesRotting(grid) == 1
