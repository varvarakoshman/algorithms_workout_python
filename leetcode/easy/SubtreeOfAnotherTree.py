# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# O(n * m) time | O(n + m) space,
# n - # nodes in a tree, m - # nodes in a subtree
class Solution:
    def isSubtree(self, root, subRoot):
        if not root:
            return False
        is_subtree = False
        if root.val == subRoot.val:
            is_subtree = self.isSameTree(root, subRoot)
        return is_subtree or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, first_node, second_node):
        if not first_node and not second_node:
            return True
        elif not first_node or not second_node:
            return False
        else:
            return first_node.val == second_node.val and self.isSameTree(first_node.left, second_node.left) and\
                   self.isSameTree(first_node.right, second_node.right)
