# Solution 1 (recursive)
# O(n) time | O(n) space
def find_closest_value_in_bst_(tree, target):
    return depth_first_search(tree, target).value


def depth_first_search(node, target):
    if node is None:
        return BST(float("inf"))
    return min(node, depth_first_search(node.left, target),
               depth_first_search(node.right, target), key=lambda n: abs(n.value - target))


# Solution 2 - optimal, iterative
# O(logn) time | O(1) space
def find_closest_value_in_bst(tree, target):
    curr_min = None
    min_diff = float("inf")
    while tree is not None:
        curr_diff = target - tree.value
        if abs(curr_diff) < min_diff:
            min_diff = abs(curr_diff)
            curr_min = tree
        tree = tree.left if curr_diff < 0 else tree.right
    return curr_min.value


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def get_root_test_tree():
    node10 = BST(10)
    node5 = BST(5)
    node10.left = node5
    node15 = BST(15)
    node10.right = node15
    node13 = BST(13)
    node22 = BST(22)
    node15.left = node13
    node15.right = node22
    node14 = BST(14)
    node13.right = node14
    node2 = BST(2)
    node5_2 = BST(5)
    node5.left = node2
    node5.right = node5_2
    node1 = BST(1)
    node2.left = node1
    return node10
    #         10
    #       /    \
    #      5      15
    #    /  \    /  \
    #   2    5  13  22
    #  /         \
    # 1           14


if __name__ == '__main__':
    assert find_closest_value_in_bst(get_root_test_tree(), 12) == 13
