# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# O(n) time | O(n) space
class Solution:

    def __init__(self):
        self.lowest_common_ancestor = None

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.is_target_node(root, p, q)
        return self.lowest_common_ancestor

    def is_target_node(self, node, p, q):
        if not node:
            return False

        is_middle = node.val == p.val or node.val == q.val
        is_in_left = self.is_target_node(node.left, p, q)
        is_in_right = self.is_target_node(node.right, p, q)

        if is_in_left and is_in_right or is_middle and (is_in_left or is_in_right):
            self.lowest_common_ancestor = node

        return is_middle or is_in_left or is_in_right

