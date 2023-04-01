import unittest


# Solution 1 (recursive)
# O(n) time | O(h) space
def invert_binary_tree(tree):
    if tree is None:
        return None
    swap_left_and_right(tree)
    invert_binary_tree(tree.left)
    invert_binary_tree(tree.right)


def swap_left_and_right(tree):
    tree.left, tree.right = tree.right, tree.left


# Solution 2 (iterative)
# O(n) time | O(h) space
def invertBinaryTree(tree):
    queue = [tree]
    while len(queue) > 0:
        node = queue.pop(0)
        swap_left_and_right(node)
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __eq__(self, other):
        return isinstance(other, type(self)) and self.__dict__ == other.__dict__

    def insert(self, values, i=0):
        if i >= len(values):
            return
        queue = [self]
        while len(queue) > 0:
            current = queue.pop(0)
            if current.left is None:
                current.left = BinaryTree(values[i])
                break
            queue.append(current.left)
            if current.right is None:
                current.right = BinaryTree(values[i])
                break
            queue.append(current.right)
        self.insert(values, i + 1)
        return self

    def invertedInsert(self, values, i=0):
        if i >= len(values):
            return
        queue = [self]
        while len(queue) > 0:
            current = queue.pop(0)
            if current.right is None:
                current.right = BinaryTree(values[i])
                break
            queue.append(current.right)
            if current.left is None:
                current.left = BinaryTree(values[i])
                break
            queue.append(current.left)
        self.invertedInsert(values, i + 1)
        return self


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        tree = BinaryTree(1).insert([2, 3, 4, 5, 6, 7, 8, 9])
        invertedTree = BinaryTree(1).invertedInsert([2, 3, 4, 5, 6, 7, 8, 9])
        invert_binary_tree(tree)
        self.assertTrue(tree.__eq__(invertedTree))