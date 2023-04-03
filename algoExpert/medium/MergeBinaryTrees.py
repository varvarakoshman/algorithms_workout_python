# This is an input class. Do not edit.
import unittest


class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# O(n) time | O(h) space, h - height
def mergeBinaryTrees(tree1, tree2):
    if tree1 and tree2:
        left_node = mergeBinaryTrees(tree1.left, tree2.left)
        right_node = mergeBinaryTrees(tree1.right, tree2.right)
        return BinaryTree(tree1.value + tree2.value, left_node, right_node)
    return tree1 or tree2


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        tree1 = BinaryTree(1)
        tree1.left = BinaryTree(3)
        tree1.left.left = BinaryTree(7)
        tree1.left.right = BinaryTree(4)
        tree1.right = BinaryTree(2)

        tree2 = BinaryTree(1)
        tree2.left = BinaryTree(5)
        tree2.left.left = BinaryTree(2)
        tree2.right = BinaryTree(9)
        tree2.right.left = BinaryTree(7)
        tree2.right.right = BinaryTree(6)

        actual = mergeBinaryTrees(tree1, tree2)
        self.assertEqual(actual.value, 2)
        self.assertEqual(actual.left.value, 8)
        self.assertEqual(actual.left.left.value, 9)
        self.assertEqual(actual.left.right.value, 4)
        self.assertEqual(actual.right.value, 11)
        self.assertEqual(actual.right.left.value, 7)
        self.assertEqual(actual.right.right.value, 6)