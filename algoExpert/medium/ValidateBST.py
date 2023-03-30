# O(n) time | O(n) space
import sys

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree):
    min = -sys.maxsize
    max = -min
    return validate_bst_helper(tree, min, max)

# rule here: each value > values on its left, <= values on its right
def validate_bst_helper(tree, min, max):
    if tree is None:
        return True
    if tree.value < min or tree.value >= max:
        return False
    return validate_bst_helper(tree.left, min, tree.value) and validate_bst_helper(tree.right, tree.value, max)


if __name__ == '__main__':
    root = BST(10)
    root.left = BST(5)
    root.left.left = BST(2)
    root.left.left.left = BST(1)
    root.left.right = BST(5)
    root.right = BST(15)
    root.right.left = BST(13)
    root.right.left.right = BST(14)
    root.right.right = BST(22)

    assert validateBst(root) is True
