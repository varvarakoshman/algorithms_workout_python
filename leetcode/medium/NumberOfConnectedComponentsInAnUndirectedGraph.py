from typing import List


# O(|V|+|E|) time | O(|V|+|E|) space
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = self.build_adj_list(edges)
        single_nodes_count = n - len(adj_list)
        visited = set()
        components_count = 0
        for node in adj_list.keys():
            if node not in visited:
                components_count += 1
                self.dfs(node, adj_list, visited)
        return components_count + single_nodes_count

    def dfs(self, node, adj_list, visited):
        visited.add(node)
        for neighbour in adj_list[node]:
            if neighbour not in visited:
                self.dfs(neighbour, adj_list, visited)

    def build_adj_list(self, edges):
        adj_list = {}
        for edge in edges:
            from_node, to_node = edge
            if from_node not in adj_list:
                adj_list[from_node] = [to_node]
            else:
                adj_list[from_node].append(to_node)
            if to_node not in adj_list:
                adj_list[to_node] = [from_node]
            else:
                adj_list[to_node].append(from_node)
        return adj_list
