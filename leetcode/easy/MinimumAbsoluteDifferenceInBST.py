# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# O(n) time | O(n) space
class Solution:

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        inorder = []
        self.get_inorder_traversal(root, inorder)

        min_diff = 1e9  # infinity
        for i in range(1, len(inorder)):
            min_diff = min(min_diff, abs(inorder[i] - inorder[i - 1]))

        return min_diff

    def get_inorder_traversal(self, node, result):
        if node:
            self.get_inorder_traversal(node.left, result)
            result.append(node.val)
            self.get_inorder_traversal(node.right, result)


# O(n) time | O(n) space (no extra list)
class Solution2:
    def __init__(self):
        self.min_diff = 1e9
        self.prev_node = None

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.get_inorder_traversal(root)
        return self.min_diff

    def get_inorder_traversal(self, node):
        if node:
            self.get_inorder_traversal(node.left)
            if self.prev_node:
                self.min_diff = min(self.min_diff, node.val - self.prev_node.val)
            self.prev_node = node
            self.get_inorder_traversal(node.right)