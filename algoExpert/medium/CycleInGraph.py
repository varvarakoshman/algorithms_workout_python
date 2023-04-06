import unittest


# O(|V| + |E|) time | O(|V|) space
def cycleInGraph(edges):
    for vertex in range(len(edges)):
        visited = [0] * len(edges)
        has_cycle = dfs(vertex, edges, visited)
        if has_cycle:
            return True
    return False


def dfs(vertex, edges, visited):
    if visited[vertex] == 1:
        return True
    visited[vertex] = 1
    neighbours = edges[vertex]
    for neighbour in neighbours:
        if visited[neighbour] != 2:
            has_cycle = dfs(neighbour, edges, visited)
            if has_cycle:
                return True
    visited[vertex] = 2
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
