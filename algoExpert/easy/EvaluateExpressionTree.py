# This is an input class. Do not edit.
import unittest


class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# O(n) time | O(h) space, h - height of the tree
def evaluateExpressionTree(tree):
    if tree.left is None and tree.right is None:
        return tree.value
    left_subtree_value = evaluateExpressionTree(tree.left)
    right_subtree_value = evaluateExpressionTree(tree.right)
    return apply_expression(left_subtree_value, right_subtree_value, tree.value)


def apply_expression(value1, value2, operator):
    if operator == -1:
        return value1 + value2
    elif operator == -2:
        return value1 - value2
    elif operator == -3:
        return int(value1 / value2)
    else:
        return value1 * value2


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        tree = BinaryTree(-1)
        tree.left = BinaryTree(2)
        tree.right = BinaryTree(-2)
        tree.right.left = BinaryTree(5)
        tree.right.right = BinaryTree(1)
        expected = 6
        actual = evaluateExpressionTree(tree)
        self.assertEqual(actual, expected)

    def test_case_2(self):
        tree = BinaryTree(-3)
        tree.left = BinaryTree(9)
        tree.right = BinaryTree(-2)
        tree.right.left = BinaryTree(4)
        tree.right.right = BinaryTree(6)
        expected = -4
        actual = evaluateExpressionTree(tree)
        self.assertEqual(actual, expected)
