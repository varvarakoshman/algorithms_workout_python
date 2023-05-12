# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# O(h) time | O(h) space
class Solution:

    def goodNodes(self, root):
        good_nodes_count = self.dfs(root, -float("inf"))
        return good_nodes_count

    def dfs(self, node, curr_max):
        if not node:
            return 0
        good_nodes = 1 if node.val >= curr_max else 0

        good_nodes += self.dfs(node.right, max(curr_max, node.val))
        good_nodes += self.dfs(node.left, max(curr_max, node.val))
        return good_nodes
