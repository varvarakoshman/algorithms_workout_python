# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# O(n) time | O(n) space
class Solution:
    def __init__(self):
        self.max_sum = -1001

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.compute_sum(root)
        return self.max_sum

    def compute_sum(self, node):
        curr_sum = node.val
        left_sum = self.compute_sum(node.left) if node.left else 0
        right_sum = self.compute_sum(node.right) if node.right else 0
        self.max_sum = max(self.max_sum, curr_sum + left_sum + right_sum)
        return max(0, max(left_sum, right_sum) + curr_sum)
