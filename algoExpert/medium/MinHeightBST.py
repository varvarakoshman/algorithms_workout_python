import unittest


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)


# Solution
##############################################################################
# O(n) time | O(n) space
def minHeightBst(array):
    return minHeightBst_helper(0, len(array) - 1, array)


def minHeightBst_helper(start, end, array):
    if start == end:
        return BST(array[start])
    central = start + (end - start) // 2
    current_root = BST(array[central])
    if central > start:
        current_root.left = minHeightBst_helper(start, central - 1, array)
    if central < end:
        current_root.right = minHeightBst_helper(central + 1, end, array)
    return current_root
##############################################################################


def getTreeHeight(tree, height=0):
    if tree is None:
        return height
    leftTreeHeight = getTreeHeight(tree.left, height + 1)
    rightTreeHeight = getTreeHeight(tree.right, height + 1)
    return max(leftTreeHeight, rightTreeHeight)


def inOrderTraverse(tree, array):
    if tree is not None:
        inOrderTraverse(tree.left, array)
        array.append(tree.value)
        inOrderTraverse(tree.right, array)
    return array


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        array = [1, 2, 5, 7, 10, 13, 14, 15, 22]
        tree = minHeightBst(array)
        self.assertEqual(getTreeHeight(tree), 4)
        inOrder = inOrderTraverse(tree, [])
        self.assertEqual(inOrder, [1, 2, 5, 7, 10, 13, 14, 15, 22])
