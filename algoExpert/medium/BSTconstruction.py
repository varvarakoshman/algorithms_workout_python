import unittest


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # def insert(self, value):
    #     curr_node = parent_node = self
    #     while curr_node is not None and \
    #             (curr_node.left is not None or curr_node.right is not None):
    #         parent_node = curr_node
    #         if value >= curr_node.value:
    #             curr_node = curr_node.right
    #         else:
    #             curr_node = curr_node.left
    #     new_node = BST(value)
    #     is_leaf = curr_node is not None and curr_node.right is None and curr_node.left is None
    #     if is_leaf:
    #         curr_node.set_child(new_node)
    #     else:
    #         parent_node.set_child(new_node)
    #     return self

    # def set_child(self, new_node):
    #     if new_node.value >= self.value:
    #         self.right = new_node
    #     else:
    #         self.left = new_node

    # Average: O(n*log(n)) | O(1) space
    # Worst: O(n) time | O(1) space
    def insert(self, value):
        curr_node = self
        while True:
            if value < curr_node.value:
                if curr_node.left is None:
                    curr_node.left = BST(value)
                    break
                else:
                    curr_node = curr_node.left
            else:
                if curr_node.right is None:
                    curr_node.right = BST(value)
                    break
                else:
                    curr_node = curr_node.right
        return self

    # Average: O(n*log(n)) | O(1) space
    # Worst: O(n) time | O(1) space
    def contains(self, value):
        curr_node = self
        while curr_node is not None:
            if value == curr_node.value:
                return True
            elif value >= curr_node.value:
                curr_node = curr_node.right
            else:
                curr_node = curr_node.left
        return False

    # Average: O(n*log(n)) | O(1) space
    # Worst: O(n) time | O(1) space
    def remove(self, value, parent_node=None):
        curr_node = self
        while curr_node is not None:
            if value == curr_node.value:
                not_leaf = curr_node.right is not None and curr_node.left is not None
                if not_leaf:
                    right_min_value = curr_node.right.get_min_value()
                    curr_node.value = right_min_value
                    curr_node.right.remove(curr_node.value, curr_node)
                elif parent_node is None:
                    if curr_node.left is not None:
                        curr_node.value = curr_node.left.value
                        curr_node.right = curr_node.left.right
                        curr_node.left = curr_node.left.left
                    elif curr_node.right is not None:
                        curr_node.value = curr_node.right.value
                        curr_node.left = curr_node.right.left
                        curr_node.right = curr_node.right.right
                    # else: # super edge case - discussable
                    #     curr_node.value = None
                elif parent_node.left == curr_node:
                    parent_node.left = curr_node.left if curr_node.left is not None else curr_node.right
                elif parent_node.right == curr_node:
                    parent_node.right = curr_node.left if curr_node.left is not None else curr_node.right
                break
            parent_node = curr_node
            if value > curr_node.value:
                curr_node = curr_node.right
            else:
                curr_node = curr_node.left
        return self

    def get_min_value(self):
        curr_node = self
        while curr_node.left is not None:
            curr_node = curr_node.left
        return curr_node.value


# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!
class TestProgram(unittest.TestCase):
    def test_case_1(self):
        root = BST(10)
        root.left = BST(5)
        root.left.left = BST(2)
        root.left.left.left = BST(1)
        root.left.right = BST(5)
        root.right = BST(15)
        root.right.left = BST(13)
        root.right.left.right = BST(14)
        root.right.right = BST(22)

        root.insert(12)
        self.assertTrue(root.right.left.left.value == 12)

        root.remove(10)
        self.assertTrue(not root.contains(10))
        self.assertTrue(root.value == 12)

        self.assertTrue(root.contains(15))

        root = BST(10)
        root.insert(5)
        root.insert(15)
        root.remove(10)

        root.insert(2)
        root.insert(5)
        root.insert(13)
        root.insert(22)
        root.insert(1)
        root.insert(14)
        root.insert(12)
        root.contains(15)
