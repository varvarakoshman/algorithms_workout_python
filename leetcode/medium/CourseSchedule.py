# O(|V| + |E|) time | O(|V|) space
class Solution:
    WHITE, GREY, BLACK = 0, 1, 2

    def canFinish(self, numCourses, prerequisites):
        visited = [self.WHITE] * numCourses
        adj_list = self.get_adj_list(prerequisites)
        for node_id in adj_list.keys():
            if visited[node_id] != self.WHITE:
                continue
            has_cycle = self.dfs(node_id, adj_list, visited)
            if has_cycle:
                return False
        return True

    def get_adj_list(self, prerequisites):
        adj_list = {}
        for pair in prerequisites:
            node_to, node_from = pair[0], pair[1]
            if node_to not in adj_list:
                adj_list[node_to] = [node_from]
            else:
                adj_list[node_to].append(node_from)
        return adj_list

    def dfs(self, node_id, adj_list, visited):
        if visited[node_id] == self.GREY:
            return True
        visited[node_id] = self.GREY
        neighbours = adj_list[node_id] if node_id in adj_list else []
        for neighbour in neighbours:
            if visited[neighbour] == self.BLACK:
                continue
            has_cycle = self.dfs(neighbour, adj_list, visited)
            if has_cycle:
                return True
        visited[node_id] = self.BLACK
        return False


if __name__ == '__main__':
    solution = Solution()

    numCourses = 2
    prerequisites = [[1, 0]]
    assert solution.canFinish(numCourses, prerequisites) is True

    numCourses = 2
    prerequisites = [[1, 0], [0, 1]]
    assert solution.canFinish(numCourses, prerequisites) is False

    numCourses = 5
    prerequisites = [[1, 2], [2, 3], [3, 4], [4, 2]]
    assert solution.canFinish(numCourses, prerequisites) is False
