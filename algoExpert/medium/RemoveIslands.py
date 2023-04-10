import unittest


# O(w*h) time | O(w*h) space, w - width, h - height
def removeIslands(matrix):
    visited = set()
    for i in range(1, len(matrix) - 1):
        for j in range(1, len(matrix[0]) - 1):
            curr_value = matrix[i][j]
            if curr_value == 0 or tuple([i, j]) in visited:
                continue
            island_points = get_island_points(i, j, matrix, visited)
            for point in island_points:
                matrix[point[0]][point[1]] = 0
    return matrix


def get_island_points(i, j, matrix, visited):
    island_points = []
    queue_nodes = [tuple([i, j])]
    is_island = True
    while len(queue_nodes) > 0:
        curr_node = queue_nodes.pop(0)
        is_island = is_island and 0 < curr_node[0] < len(matrix) - 1 and 0 < curr_node[1] < len(matrix[0]) - 1
        if not is_island:
            visited.add(curr_node)
            continue
        island_points.append(curr_node)
        visited.add(curr_node)
        island_neighbours = get_neighbours(curr_node, matrix, visited)
        for neighbour in island_neighbours:
            queue_nodes.append(neighbour)
    return island_points if is_island else []


def get_neighbours(curr_node, matrix, visited):
    neighbours = []
    i, j = curr_node
    if matrix[i + 1][j] == 1 and tuple([i + 1, j]) not in visited:
        neighbours.append(tuple([i + 1, j]))
    if matrix[i - 1][j] == 1 and tuple([i - 1, j]) not in visited:
        neighbours.append(tuple([i - 1, j]))
    if matrix[i][j - 1] == 1 and tuple([i, j - 1]) not in visited:
        neighbours.append(tuple([i, j - 1]))
    if matrix[i][j + 1] == 1 and tuple([i, j + 1]) not in visited:
        neighbours.append(tuple([i, j + 1]))
    return neighbours


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = [
            [1, 0, 0, 0, 0, 0],
            [0, 1, 0, 1, 1, 1],
            [0, 0, 1, 0, 1, 0],
            [1, 1, 0, 0, 1, 0],
            [1, 0, 1, 1, 0, 0],
            [1, 0, 0, 0, 0, 1],
        ]
        expected = [
            [1, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 1],
            [0, 0, 0, 0, 1, 0],
            [1, 1, 0, 0, 1, 0],
            [1, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 1],
        ]
        actual = removeIslands(input)
        self.assertEqual(actual, expected)
