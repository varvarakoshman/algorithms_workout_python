import unittest


# O(|V| + |E|) time | O(|V|) space
def twoColorable(edges):
    nodes_queue = [0]
    colors = [0] * len(edges)
    colors[0] = 1
    while len(nodes_queue) > 0:
        curr_node = nodes_queue.pop(0)
        neighbours = edges[curr_node]
        neighbour_color = 2 if colors[curr_node] == 1 else 1
        for neighbour in neighbours:
            if colors[curr_node] == colors[neighbour]:
                return False
            if colors[neighbour] == 0:
                nodes_queue.append(neighbour)
                colors[neighbour] = neighbour_color
    return True


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = [[1], [0]]
        expected = True
        actual = twoColorable(input)
        self.assertEqual(actual, expected)

    def test_case_2(self):
        input = [[1, 2], [0, 2], [0, 1]]
        expected = False
        actual = twoColorable(input)
        self.assertEqual(actual, expected)

    def test_case_3(self):
        input = [[1], [1]]
        expected = False
        actual = twoColorable(input)
        self.assertEqual(actual, expected)

    def test_case_4(self):
        input = [[1, 2], [0, 3], [0, 3], [1, 2]]
        expected = True
        actual = twoColorable(input)
        self.assertEqual(actual, expected)

    def test_case_5(self):
        input = [[1, 2, 3], [0, 4], [0, 4], [0, 2], [1, 2]]
        expected = False
        actual = twoColorable(input)
        self.assertEqual(actual, expected)
