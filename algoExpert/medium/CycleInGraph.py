import unittest

# Solution 1 (with colors)
# O(|V| + |E|) time | O(|V|) space

WHITE, GREY, BLACK = 0, 1, 2


def cycleInGraph_(edges):
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
        if visited[neighbour] == BLACK:
            continue
        has_cycle = dfs(neighbour, edges, visited)
        if has_cycle:
            return True
    visited[vertex] = BLACK
    return False


# Solution 2 (with stack)
# O(|V| + |E|) time | O(|V|) space
def cycleInGraph(edges):
    number_of_nodes = len(edges)
    visited = [False for _ in range(number_of_nodes)]
    currently_in_stack = [False for _ in range(number_of_nodes)]

    for node in range(number_of_nodes):
        if visited[node]:
            continue

        contains_cycle = is_node_in_cycle(node, edges, visited, currently_in_stack)
        if contains_cycle:
            return True

    return False


def is_node_in_cycle(node, edges, visited, currently_in_stack):
    visited[node] = True
    currently_in_stack[node] = True

    neighbours = edges[node]
    for neighbour in neighbours:
        if not visited[neighbour]:
            contains_cycle = is_node_in_cycle(neighbour, edges, visited, currently_in_stack)
            if contains_cycle:
                return True
        elif currently_in_stack[neighbour]:
            return True

    currently_in_stack[node] = False
    return False


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = [[1, 3], [2, 3, 4], [0], [], [2, 5], []]
        expected = True
        actual = cycleInGraph(input)
        self.assertEqual(actual, expected)

    def test_case_2(self):
        input = [[1, 2], [2], []]
        expected = False
        actual = cycleInGraph(input)
        self.assertEqual(actual, expected)

    def test_case_3(self):
        input = [[1, 2], [2], [1]]
        expected = True
        actual = cycleInGraph(input)
        self.assertEqual(actual, expected)

    def test_case_4(self):
        input = [[0], [1]]
        expected = True
        actual = cycleInGraph(input)
        self.assertEqual(actual, expected)

    def test_case_5(self):
        input = [[0]]
        expected = True
        actual = cycleInGraph(input)
        self.assertEqual(actual, expected)
