# This is an input class. Do not edit.
import unittest


class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class TreeInfo:
    def __init__(self, is_balanced, height):
        self.is_balanced = is_balanced
        self.height = height


# O(n) time | O(h) space, h - height
def heightBalancedBinaryTree(tree):
    tree_info = get_tree_info(tree)
    return tree_info.is_balanced


# O(n) time | O(h) space, h - height
def get_tree_info(tree):
    if tree is None:
        return TreeInfo(True, 0)

    left_tree_info = get_tree_info(tree.left)
    right_tree_info = get_tree_info(tree.right)

    is_balanced = left_tree_info.is_balanced and right_tree_info.is_balanced \
                  and abs(left_tree_info.height - right_tree_info.height) <= 1
    height = max(left_tree_info.height, right_tree_info.height) + 1

    return TreeInfo(is_balanced, height)


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        root = BinaryTree(1)
        root.left = BinaryTree(2)
        root.right = BinaryTree(3)
        root.left.left = BinaryTree(4)
        root.left.right = BinaryTree(5)
        root.right.right = BinaryTree(6)
        root.left.right.left = BinaryTree(7)
        root.left.right.right = BinaryTree(8)
        expected = True
        actual = heightBalancedBinaryTree(root)
        self.assertEqual(actual, expected)

    def test_case_2(self):
        root = BinaryTree(1)
        root.left = BinaryTree(2)
        root.right = BinaryTree(3)
        root.left.left = BinaryTree(4)
        root.left.left.left = BinaryTree(6)
        root.right.right = BinaryTree(5)
        expected = False
        actual = heightBalancedBinaryTree(root)
        self.assertEqual(actual, expected)
