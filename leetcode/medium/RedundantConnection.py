# O(|V|^2) time | O(|V| + |E|) space
class Solution1:
    def findRedundantConnection(self, edges):
        adj_list = {}
        latest_reachable = None
        for edge in edges:
            visited = set()
            node_from, node_to = edge
            is_nodes_present = node_from in adj_list and node_to in adj_list
            if is_nodes_present and self.check_if_reachable_dfs(adj_list, visited, node_from, node_to):
                latest_reachable = edge
            self.add_connection(adj_list, node_to, node_from)
            self.add_connection(adj_list, node_from, node_to)
        return latest_reachable

    def add_connection(self, adj_list, node_to, node_from):
        if node_to not in adj_list:
            adj_list[node_to] = []
        adj_list[node_to].append(node_from)

    # check if path between source and target exists
    def check_if_reachable_dfs(self, adj_list, visited, source, target):
        if source == target:
            return True
        neighbours = adj_list[source]
        visited.add(source)
        is_reachable = False
        for neighbour in neighbours:
            if neighbour in visited:
                continue
            is_reachable = is_reachable or self.check_if_reachable_dfs(adj_list, visited, neighbour, target)
            if is_reachable:
                break
        return is_reachable


# O(α(n) * |V|) ~ O(|V|) time | O(α(n)) ~ O(|V|) space
class Solution2:
    def findRedundantConnection(self, edges):
        union_find = UnionFind()
        latest_redundant = None
        for edge in edges:
            node_from, node_to = edge
            parent_from = union_find.find(node_from)
            parent_to = union_find.find(node_to)
            if parent_from and parent_to and parent_to == parent_from:
                latest_redundant = edge
            else:
                if not parent_from:
                    union_find.create(node_from)
                if not parent_to:
                    union_find.create(node_to)
                union_find.union(node_to, node_from)
        return latest_redundant


class UnionFind:

    def __init__(self):
        self.parents = {}
        self.ranks = {}

    # O(1) time | O(1) space
    def create(self, value):
        self.parents[value] = value
        self.ranks[value] = 0

    # O(α(n)) ~ O(1) time | O(α(n)) ~ O(1) space
    def find(self, value):
        if value not in self.parents:
            return None

        while self.parents[value] != value:
            self.parents[value] = self.find(self.parents[value])
            value = self.parents[value]
        return value

    # O(α(n)) ~ O(1) time | O(α(n)) ~ O(1) space
    def union(self, value_one, value_two):
        if value_one not in self.parents or value_two not in self.parents:
            return

        representative_one = self.find(value_one)
        representative_two = self.find(value_two)

        if self.ranks[representative_two] > self.ranks[representative_one]:
            self.parents[representative_one] = representative_two
        elif self.ranks[representative_two] < self.ranks[representative_one]:
            self.parents[representative_two] = representative_one
        else:
            self.parents[representative_two] = representative_one
            self.ranks[representative_two] += 1


if __name__ == '__main__':
    solutions = [Solution1(), Solution2()]

    for solution in solutions:
        edges = [[9, 10], [5, 8], [2, 6], [1, 5], [3, 8], [4, 9], [8, 10], [4, 10], [6, 8], [7, 9]]
        assert solution.findRedundantConnection(edges) == [4, 10]

        edges = [[1, 2], [1, 3], [2, 3]]
        assert solution.findRedundantConnection(edges) == [2, 3]

        edges = [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]
        assert solution.findRedundantConnection(edges) == [1, 4]
