# O(|V| + |E|) time | O(|V| + |E|) space
class Solution:
    WHITE, GREY, BLACK = 0, 1, 2

    def findOrder(self, numCourses, prerequisites):
        adj_list = self.get_adj_list(numCourses, prerequisites)
        has_cycle = self.check_has_cycle(numCourses, adj_list)
        if has_cycle:
            return []
        return self.topological_sort(adj_list)

    def get_adj_list(self, numCourses, prerequisites):
        adj_list = {}
        for i in range(numCourses):
            adj_list[i] = []
        for pair in prerequisites:
            to_node, from_node = pair[0], pair[1]
            adj_list[from_node].append(to_node)
        return adj_list

    def check_has_cycle(self, numCourses, adj_list):
        visited = [self.WHITE] * numCourses
        for node_id in adj_list.keys():
            if visited[node_id] != self.WHITE:
                continue
            has_cycle = self.dfs_cycle(node_id, adj_list, visited)
            if has_cycle:
                return True
        return False

    def dfs_cycle(self, node_id, adj_list, visited):
        if visited[node_id] == self.GREY:
            return True
        visited[node_id] = self.GREY
        for neighbour in adj_list[node_id]:
            if visited[neighbour] == self.BLACK:
                continue
            has_cycle = self.dfs_cycle(neighbour, adj_list, visited)
            if has_cycle:
                return True
        visited[node_id] = self.BLACK
        return False

    def topological_sort(self, adj_list):
        sorted_vertices = []
        visited = set()
        for node_id in adj_list.keys():
            if node_id not in visited:
                self.dfs(node_id, adj_list, visited, sorted_vertices)
        sorted_vertices.reverse()
        return sorted_vertices

    def dfs(self, node_id, adj_list, visited, path):
        visited.add(node_id)
        for neighbour in adj_list[node_id]:
            if neighbour not in visited:
                self.dfs(neighbour, adj_list, visited, path)
        path.append(node_id)


if __name__ == '__main__':
    solution = Solution()

    numCourses = 2
    prerequisites = [[1, 0]]
    assert solution.findOrder(numCourses, prerequisites) == [0, 1]

    numCourses = 4
    prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
    assert solution.findOrder(numCourses, prerequisites) == [0, 2, 1, 3]

    numCourses = 1
    prerequisites = []
    assert solution.findOrder(numCourses, prerequisites) == [0]

    # numCourses = 8
    # prerequisites = [[2, 1], [3, 2], [7, 2], [4, 3], [4, 5], [2, 5]]

