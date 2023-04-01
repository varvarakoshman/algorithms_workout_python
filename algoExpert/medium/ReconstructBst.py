# This is an input class. Do not edit.
import unittest


class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class TreeInfo:
    def __init__(self, root_idx):
        self.root_idx = root_idx


# O(n) time | O(n + h) space
def reconstruct_bst(preorder_traversal_values):
    tree_info = TreeInfo(0)
    return reconstruct_bst_from_range(float('-inf'), float('inf'), preorder_traversal_values, tree_info)


def reconstruct_bst_from_range(lower_bound, upper_bound, array, tree_info):
    if tree_info.root_idx > len(array) - 1:
        return None
    root_value = array[tree_info.root_idx]
    if root_value < lower_bound or root_value >= upper_bound:
        return None
    tree_info.root_idx += 1

    left_subtree = reconstruct_bst_from_range(lower_bound, root_value, array, tree_info)
    right_subtree = reconstruct_bst_from_range(root_value, upper_bound, array, tree_info)
    return BST(root_value, left_subtree, right_subtree)


def getDfsOrder(node, values):
    if node is None:
        return
    values.append(node.value)
    getDfsOrder(node.left, values)
    getDfsOrder(node.right, values)
    return values


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        preorder_traversal_values = [10, 4, 2, 1, 3, 17, 19, 18]
        tree = BST(10)
        tree.left = BST(4)
        tree.left.left = BST(2)
        tree.left.left.left = BST(1)
        tree.left.right = BST(3)
        tree.right = BST(17)
        tree.right.right = BST(19)
        tree.right.right.left = BST(18)
        expected = getDfsOrder(tree, [])
        actual = reconstruct_bst(preorder_traversal_values)
        actual_dfs_order = getDfsOrder(actual, [])
        self.assertEqual(actual_dfs_order, expected)
