# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# O(n) time | O(n) space
class Solution1:

    def flatten(self, root) -> None:
        self.flatten_tree(root)

    def flatten_tree(self, node):
        if not node or not node.left and not node.right:
            return node

        left_tail = self.flatten_tree(node.left)
        right_tail = self.flatten_tree(node.right)

        if left_tail:
            left_tail.right = node.right
            node.right = node.left
            node.left = None

        return right_tail if right_tail else left_tail


# O(n) time | O(1) space
class Solution2:
    def flatten(self, root) -> None:
        curr = root
        while curr:
            if curr.left:
                right_most = self.get_right_most(curr.left)
                right_most.right = curr.right
                curr.right = curr.left
                curr.left = None
            curr = curr.right

    def get_right_most(self, node):
        while node:
            if not node.right:
                break
            node = node.right
        return node


if __name__ == '__main__':
    def get_test_tree():
        one = TreeNode(1)
        two = TreeNode(2)
        three = TreeNode(3)
        four = TreeNode(4)
        five = TreeNode(5)
        six = TreeNode(6)

        one.left = two
        one.right = five
        two.left = three
        two.right = four
        five.right = six
        return one

    solutions = [Solution1(), Solution2()]
    for solution in solutions:
        solution.flatten(get_test_tree())
