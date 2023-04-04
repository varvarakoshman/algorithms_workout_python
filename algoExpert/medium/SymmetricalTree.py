# This is an input class. Do not edit.
import unittest


class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# O(n) time | O(h) space
def symmetrical_tree(tree):
    return check_trees_symmetric(tree.left, tree.right, True)


def check_trees_symmetric(left_tree, right_tree, is_symmetric):
    if not is_symmetric:
        return is_symmetric
    if left_tree is not None and right_tree is not None and left_tree.value == right_tree.value:
        return check_trees_symmetric(left_tree.right, right_tree.left, is_symmetric) and \
               check_trees_symmetric(left_tree.left, right_tree.right, is_symmetric)
    return left_tree == right_tree


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        tree = BinaryTree(10)
        tree.left = BinaryTree(5)
        tree.right = BinaryTree(5)
        tree.left.left = BinaryTree(7)
        tree.left.right = BinaryTree(9)
        tree.right.left = BinaryTree(9)
        tree.right.right = BinaryTree(7)
        expected = True
        actual = symmetrical_tree(tree)
        self.assertEqual(actual, expected)