from typing import List


# O(n^2) time | O(n) space
class Solution:
    def findCircleNum(self, adj_matrix: List[List[int]]) -> int:
        visited = set()
        components_count = 0
        n_vertices = len(adj_matrix)
        for vertex in range(n_vertices):
            if vertex not in visited:
                self.dfs(vertex, adj_matrix, visited)
                components_count += 1
        return components_count

    def dfs(self, node, adj_matrix, visited):
        visited.add(node)
        for neigh in range(len(adj_matrix)):
            if adj_matrix[node][neigh] == 1 and neigh not in visited:
                self.dfs(neigh, adj_matrix, visited)