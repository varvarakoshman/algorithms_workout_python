import unittest


# O(|V| + |E|) time | O(|V|) space

WHITE, GREY, BLACK = 0, 1, 2


def cycleInGraph(edges):
    number_of_nodes = len(edges)
    visited = [WHITE] * number_of_nodes
    for vertex in range(number_of_nodes):
        if visited[vertex] != WHITE:
            continue
        has_cycle = dfs(vertex, edges, visited)
        if has_cycle:
            return True
    return False


def dfs(vertex, edges, visited):
    if visited[vertex] == GREY:
        return True
    visited[vertex] = GREY
    neighbours = edges[vertex]
    for neighbour in neighbours:
        if visited[neighbour] == GREY:
            return True
        if visited[neighbour] != WHITE:
            continue
        has_cycle = dfs(neighbour, edges, visited)
        if has_cycle:
            return True
    visited[vertex] = BLACK
    return False


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = [[1, 3], [2, 3, 4], [0], [], [2, 5], []]
        expected = True
        actual = cycleInGraph(input)
        self.assertEqual(actual, expected)

        input = [[1, 2], [2], []]
        expected = False
        actual = cycleInGraph(input)
        self.assertEqual(actual, expected)

        input = [[1, 2], [2], [1]]
        expected = True
        actual = cycleInGraph(input)
        self.assertEqual(actual, expected)

        input = [[0], [1]]
        expected = True
        actual = cycleInGraph(input)
        self.assertEqual(actual, expected)

        input = [[0]]
        expected = True
        actual = cycleInGraph(input)
        self.assertEqual(actual, expected)
