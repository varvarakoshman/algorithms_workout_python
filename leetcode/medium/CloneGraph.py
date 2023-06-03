class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


# O(|V| + |E|) time | O(|V|) space
class Solution:
    def cloneGraph(self, node):
        new_nodes_mapping = {}

        def dfs(node):
            if not node:
                return None
            if node.val in new_nodes_mapping:
                return new_nodes_mapping[node.val]

            new_node = Node(node.val)
            new_nodes_mapping[node.val] = new_node

            new_neighbours = []
            for neighbour in node.neighbors:
                new_neighbours.append(dfs(neighbour))
            new_node.neighbors = new_neighbours

            return new_node

        return dfs(node)


if __name__ == '__main__':
    solution = Solution()
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node1.neighbors = [node2, node4]
    node2.neighbors = [node1, node3]
    node3.neighbors = [node2, node4]
    node4.neighbors = [node1, node3]

    cloned_graph = solution.cloneGraph(node1)
