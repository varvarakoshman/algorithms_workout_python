# This is an input class. Do not edit.
import unittest


class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def binaryTreeDiameter(tree):
    tree_info = TreeInfo()
    dfs(tree, tree_info, 1)
    return tree_info.diameter


class TreeInfo:
    def __init__(self):
        self.diameter = 0


# O(n) time | O(h) space
def dfs(node, tree_info, depth):
    if node.left is None and node.right is None:
        return depth

    left_longest_path = dfs(node.left, tree_info, depth + 1) if node.left is not None else 0
    right_longest_path = dfs(node.right, tree_info, depth + 1) if node.right is not None else 0

    curr_path_len = left_longest_path + right_longest_path
    if left_longest_path > 0:
        curr_path_len -= depth
    if right_longest_path > 0:
        curr_path_len -= depth
    tree_info.diameter = max(tree_info.diameter, curr_path_len)

    return max(left_longest_path, right_longest_path)


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        root = BinaryTree(1)
        root.left = BinaryTree(3)
        root.left.left = BinaryTree(7)
        root.left.left.left = BinaryTree(8)
        root.left.left.left.left = BinaryTree(9)
        root.left.right = BinaryTree(4)
        root.left.right.right = BinaryTree(5)
        root.left.right.right.right = BinaryTree(6)
        root.right = BinaryTree(2)
        expected = 6
        actual = binaryTreeDiameter(root)
        self.assertEqual(actual, expected)
