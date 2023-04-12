# This is an input class. Do not edit.
import unittest


class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# O(n) time | O(h) space, h - height of the binary tree
# can also be solved without an auxiliary set, but with 2 passes of tree instead of 1
# firstly compute sum of the whole tree, and then search for the sum/2 in sums of the subtrees during the 2nd pass
# trade-off between time and space
def splitBinaryTree(tree):
    all_sums = set()
    whole_tree_sum = dfs(tree, all_sums)
    if whole_tree_sum % 2 != 0:
        return 0
    half_tree_sum = whole_tree_sum / 2
    return half_tree_sum if half_tree_sum in all_sums else 0


def dfs(tree, all_sums):
    if tree is None:
        return 0
    sum_left = dfs(tree.left, all_sums)
    sum_right = dfs(tree.right, all_sums)
    curr_sum = sum_left + sum_right + tree.value
    all_sums.add(curr_sum)
    return curr_sum


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        tree = BinaryTree(2)
        tree.left = BinaryTree(4)
        tree.left.left = BinaryTree(4)
        tree.left.right = BinaryTree(6)
        tree.right = BinaryTree(10)
        tree.right.left = BinaryTree(3)
        tree.right.right = BinaryTree(3)
        expected = 16
        actual = splitBinaryTree(tree)
        self.assertEqual(actual, expected)
