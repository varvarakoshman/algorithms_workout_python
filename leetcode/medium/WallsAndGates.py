from collections import deque
from typing import (
    List,
)


class Solution1:
    INF = 2 ** 31 - 1

    """
    @param rooms: m x n 2D grid
    @return: nothing
    """

    # O(|V|^2) time | O(|V|) space
    def walls_and_gates(self, rooms: List[List[int]]):
        N_ROWS, N_COLS = len(rooms), len(rooms[0])

        for i in range(N_ROWS):
            for j in range(N_COLS):
                if rooms[i][j] != self.INF:
                    continue
                curr_node = tuple([i, j])
                path = self.bfs(curr_node, rooms)
                for node_idx in range(len(path)):
                    node = path[node_idx]
                    rooms[node[0]][node[1]] = node_idx + 1

    def bfs(self, curr_node, rooms):
        def get_valid_neighbours(node, parent_node):
            i, j = node
            neighbours = [tuple([i - 1, j]), tuple([i + 1, j]), tuple([i, j - 1]), tuple([i, j + 1])]
            valid_neighbours = []
            for neighbour in neighbours:
                if check_if_valid(neighbour) and neighbour not in predecessors \
                        and rooms[neighbour[0]][neighbour[1]] != -1:
                    valid_neighbours.append(neighbour)
                    predecessors[neighbour] = parent_node
            return valid_neighbours

        def check_if_valid(node):
            return 0 <= node[0] < len(rooms) and 0 <= node[1] < len(rooms[0])

        queue = [curr_node]
        predecessors = {curr_node: None}
        while len(queue) > 0:
            curr_node = queue.pop(0)
            if rooms[curr_node[0]][curr_node[1]] == 0:
                break
            queue.extend(get_valid_neighbours(curr_node, curr_node))
        reconstructed_path = self.construct_path(predecessors, curr_node)
        return reconstructed_path

    def construct_path(self, predecessors, curr_node):
        path = []
        parent = predecessors[curr_node]
        while parent:
            path.append(parent)
            curr_node = parent
            parent = predecessors[curr_node]
        return path


# O(|V|) time | O(|V|) space
class Solution2:

    def walls_and_gates(self, rooms: List[List[int]]):
        N_ROWS, N_COLS = len(rooms), len(rooms[0])
        visited = set()
        queue = deque()

        def add_room(r, c):
            if r < 0 or c < 0 or r >= N_ROWS or c >= N_COLS or (r, c) in visited or rooms[r][c] == -1:
                return
            curr_node = (r, c)
            queue.append(curr_node)
            visited.add(curr_node)

        for i in range(N_ROWS):
            for j in range(N_COLS):
                if rooms[i][j] == 0:
                    queue.append([i, j])
                    visited.add((i, j))

        distance = 0
        while len(queue) > 0:
            for i in range(len(queue)):
                row, column = queue.popleft()
                rooms[row][column] = distance
                add_room(row + 1, column)
                add_room(row - 1, column)
                add_room(row, column + 1)
                add_room(row, column - 1)
            distance += 1


if __name__ == '__main__':
    solutions = [Solution1(), Solution2()]

    for solution in solutions:
        grid = [[2147483647, -1, 0, 2147483647],
                [2147483647, 2147483647, 2147483647, -1],
                [2147483647, -1, 2147483647, -1],
                [0, -1, 2147483647, 2147483647]]
        expected = [[3, -1, 0, 1],
                    [2, 2, 1, -1],
                    [1, -1, 2, -1],
                    [0, -1, 3, 4]]
        solution.walls_and_gates(grid)
        assert grid == expected

        grid = [[0, -1],
                [2147483647, 2147483647]]
        expected = [[0, -1],
                    [1, 2]]
        solution.walls_and_gates(grid)
        assert grid == expected
