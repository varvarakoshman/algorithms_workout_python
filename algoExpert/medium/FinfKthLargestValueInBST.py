import unittest


class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# O(h + k) time | O(h) space
# Recursive solution
# (my solution)
def findKthLargestValueInBst_(tree, k):
    target, _ = findKthLargestValueInBst_helper(tree, k, tree)
    return target.value


def findKthLargestValueInBst_helper(tree, k, target):
    if tree is None:
        return target, k
    target, k = findKthLargestValueInBst_helper(tree.right, k, target)
    if k > 0:
        if k == 1:
            return tree, k - 1
        k -= 1
        target, k = findKthLargestValueInBst_helper(tree.left, k, target)
    return target, k


class TreeInfo:
    def __init__(self, numberOfNodesVisited, latestVisitedNodeValue):
        self.numberOfNodesVisited = numberOfNodesVisited
        self.latestVisitedNodeValue = latestVisitedNodeValue


# O(h + k) time | O(h) space
# Recursive solution
# (solution from video explanation)
def findKthLargestValueInBst(tree, k):
    tree_info = TreeInfo(0, -1)
    reverse_in_order_traverse(tree, k, tree_info)
    return tree_info.latestVisitedNodeValue


def reverse_in_order_traverse(tree, k, tree_info):
    if tree is None or tree_info.numberOfNodesVisited >= k:
        return
    reverse_in_order_traverse(tree.right, k, tree_info)
    if tree_info.numberOfNodesVisited < k:
        tree_info.numberOfNodesVisited = tree_info.numberOfNodesVisited + 1
        tree_info.latestVisitedNodeValue = tree.value
        reverse_in_order_traverse(tree.left, k, tree_info)


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        root = BST(15)
        root.left = BST(5)
        root.left.left = BST(2)
        root.left.left.left = BST(1)
        root.left.left.right = BST(3)
        root.left.right = BST(5)
        root.right = BST(20)
        root.right.left = BST(17)
        root.right.right = BST(22)

        actual = findKthLargestValueInBst_(root, 2)
        self.assertEqual(20, actual)
        actual = findKthLargestValueInBst_(root, 3)
        self.assertEqual(17, actual)
        actual = findKthLargestValueInBst_(root, 4)
        self.assertEqual(15, actual)
        actual = findKthLargestValueInBst_(root, 6)
        self.assertEqual(5, actual)
        actual = findKthLargestValueInBst_(root, 5)
        self.assertEqual(5, actual)
