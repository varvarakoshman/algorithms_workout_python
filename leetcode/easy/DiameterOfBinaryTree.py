# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


#####################################################################################
class TreeInfo:
    def __init__(self, height, diameter):
        self.height = height
        self.diameter = diameter


# O(n) time | O(h) space
class Solution:
    def diameterOfBinaryTree(self, root):
        tree_info = self.get_tree_info(root)
        return tree_info.diameter

    def get_tree_info(self, root):
        if not root:
            return TreeInfo(0, 0)
        tree_info_left = self.get_tree_info(root.left)
        tree_info_right = self.get_tree_info(root.right)
        max_diameter_so_far = max(tree_info_left.diameter, tree_info_right.diameter)
        curr_diameter = tree_info_left.height + tree_info_right.height
        curr_height = max(tree_info_left.height, tree_info_right.height) + 1
        return TreeInfo(curr_height, max(max_diameter_so_far, curr_diameter))


#####################################################################################
class TreeInfo:
    def __init__(self):
        self.diameter = 0


# O(n) time | O(h) space
class Solution:
    def diameterOfBinaryTree(self, root):
        tree_info = TreeInfo()
        self.traverse(root, tree_info)
        return tree_info.diameter

    def traverse(self, root, tree_info):
        if not root:
            return 0
        left_depth = self.traverse(root.left, tree_info)
        right_depth = self.traverse(root.right, tree_info)
        curr_diameter = left_depth + right_depth
        tree_info.diameter = max(tree_info.diameter, curr_diameter)
        return max(left_depth, right_depth) + 1