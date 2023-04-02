# This is an input class. Do not edit.
import unittest


class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


# O(h) time | O(1) space
def findSuccessor(tree, node):
    if node.right is not None:
        return find_left_most(node.right)
    elif node.parent is not None:
        return find_right_most(node)
    return None


def find_left_most(tree):
    while tree.left is not None:
        tree = tree.left
    return tree


def find_right_most(tree):
    if tree.parent.right == tree:
        return tree.parent.parent
    else:
        return tree.parent


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        root = BinaryTree(1)
        root.left = BinaryTree(2)
        root.left.parent = root
        root.right = BinaryTree(3)
        root.right.parent = root
        root.left.left = BinaryTree(4)
        root.left.left.parent = root.left
        root.left.right = BinaryTree(5)
        root.left.right.parent = root.left
        root.left.left.left = BinaryTree(6)
        root.left.left.left.parent = root.left.left
        node = root.left.right
        expected = root
        actual = findSuccessor(root, node)
        self.assertEqual(actual, expected)
