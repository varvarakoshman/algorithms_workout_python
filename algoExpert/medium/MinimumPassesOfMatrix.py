import unittest


# O(w * h) time | O(w * h) space
def minimumPassesOfMatrix(matrix):
    convert_queue, negative_count = get_all_positive_values(matrix)
    passes_count = 0
    already_converted = []
    while len(convert_queue) > 0 and negative_count != 0:
        curr_num_nodes = len(convert_queue)
        while curr_num_nodes > 0:
            curr_node = convert_queue.pop(0)  # O(n) time operation
            curr_num_nodes -= 1
            new_converted = get_converted_neighbours(curr_node, matrix, already_converted)
            for node in new_converted:
                if node not in already_converted:
                    convert_queue.append(node)
                    already_converted.append(node)
                    negative_count -= 1
        passes_count += 1
    return passes_count if negative_count == 0 else -1


def get_all_positive_values(matrix):
    positive_values = []
    negative_count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] > 0:
                positive_values.append(tuple([i, j]))
            elif matrix[i][j] < 0:
                negative_count += 1
    return positive_values, negative_count


def get_converted_neighbours(curr_node, matrix, already_converted):
    new_converted_nodes = []
    neighbours = get_neighbours(curr_node, len(matrix), len(matrix[0]))
    for neighbour in neighbours:
        if matrix[neighbour[0]][neighbour[1]] < 0 and neighbour not in already_converted:
            new_converted_nodes.append(neighbour)
    return new_converted_nodes


def get_neighbours(curr_node, n_rows, n_columns):
    curr_i, curr_j = curr_node[0], curr_node[1]
    neighbours = []
    if curr_i + 1 < n_rows:
        neighbours.append(tuple([curr_i + 1, curr_j]))
    if curr_i - 1 >= 0:
        neighbours.append(tuple([curr_i - 1, curr_j]))
    if curr_j - 1 >= 0:
        neighbours.append(tuple([curr_i, curr_j - 1]))
    if curr_j + 1 < n_columns:
        neighbours.append(tuple([curr_i, curr_j + 1]))
    return neighbours


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = [
            [0, -1, -3, 2, 0],
            [1, -2, -5, -1, -3],
            [3, 0, 0, -4, -1],
        ]
        expected = 3
        actual = minimumPassesOfMatrix(input)
        self.assertEqual(actual, expected)

    def test_case_2(self):
        input = [
            [0, -2, -1],
            [-5, 2, 0],
            [-6, -2, 0],
        ]
        expected = 2
        actual = minimumPassesOfMatrix(input)
        self.assertEqual(actual, expected)

    def test_case_3(self):
        input = [
            [-2, 0, -1, 1],
            [-2, -1, -1, -1]
        ]
        expected = 5
        actual = minimumPassesOfMatrix(input)
        self.assertEqual(actual, expected)
