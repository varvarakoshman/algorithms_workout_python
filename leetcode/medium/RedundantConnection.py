# O(|V|^2) time | O(|V| + |E|) space
class Solution:
    def findRedundantConnection(self, edges):
        adj_list = {}
        latest_reachable = []
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


if __name__ == '__main__':
    solution = Solution()

    edges = [[9, 10], [5, 8], [2, 6], [1, 5], [3, 8], [4, 9], [8, 10], [4, 10], [6, 8], [7, 9]]
    assert solution.findRedundantConnection(edges) == [4, 10]

    edges = [[1, 2], [1, 3], [2, 3]]
    assert solution.findRedundantConnection(edges) == [2, 3]

    edges = [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]
    assert solution.findRedundantConnection(edges) == [1, 4]
