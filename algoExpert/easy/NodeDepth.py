def node_depths(root):
    return depth_first_search(root, 0)


def depth_first_search(node, depth):
    if node is None:
        return 0
    else:
        return depth + depth_first_search(node.left, depth + 1) + depth_first_search(node.right, depth + 1)


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # complexity: O(n)
    # space complexity: O(h)


def get_root_test_tree():
    node1 = BinaryTree(1)
    node2 = BinaryTree(2)
    node1.left = node2
    node3 = BinaryTree(3)
    node1.right = node3
    node6 = BinaryTree(6)
    node7 = BinaryTree(7)
    node3.left = node6
    node3.right = node7
    node4 = BinaryTree(4)
    node5 = BinaryTree(5)
    node2.left = node4
    node2.right = node5
    node8 = BinaryTree(8)
    node9 = BinaryTree(9)
    node4.left = node8
    node4.right = node9
    return node1
    #          1
    #       /    \
    #      2      3
    #    /  \    /  \
    #   4    5  6    7
    #  /  \
    # 8    9


if __name__ == '__main__':
    assert node_depths(get_root_test_tree()) == 16
