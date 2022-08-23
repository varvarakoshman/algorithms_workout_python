def branch_sums(root):
    sums = []
    fill_branch_sums_dfs(root, 0, sums)
    return sums


def fill_branch_sums_dfs(node, curr_sum, sums):
    if node is None:
        return
    if node.left is None and node.right is None:
        sums.append(curr_sum + node.value)
    else:
        curr_sum += node.value
        fill_branch_sums_dfs(node.left, curr_sum, sums)
        fill_branch_sums_dfs(node.right, curr_sum, sums)


# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # complexity: O(n)
    # space complexity: O(n)


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
    node10 = BinaryTree(10)
    node5.left = node10
    return node1
    #          1
    #       /    \
    #      2      3
    #    /  \    /  \
    #   4    5  6    7
    #  / \   /
    # 8   9  10


if __name__ == '__main__':
    assert branch_sums(get_root_test_tree()) == [15, 16, 18, 10, 11]
