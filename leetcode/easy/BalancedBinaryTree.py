# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# def: A height-balanced binary tree is a binary tree
# in which the depth of the two subtrees of every node never differs by more than one.

class TreeNodeInfo:
    def __init__(self, is_valid, depth):
        self.is_valid = is_valid
        self.depth = depth


# O(n) time | O(h) space
class Solution:
    def isBalanced(self, root):
        return self.isBalanced(root).is_valid

    def isBalanced_helper(self, root):
        if not root:
            return TreeNodeInfo(True, 0)
        info_left = self.isBalanced_helper(root.left)
        info_right = self.isBalanced_helper(root.right)

        node_depth = max(info_left.depth, info_right.depth)
        if abs(info_left.depth - info_right.depth) > 1:
            return TreeNodeInfo(False, node_depth + 1)
        else:
            return TreeNodeInfo(info_left.is_valid and info_right.is_valid, node_depth + 1)
