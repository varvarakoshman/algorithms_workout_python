# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# O(n) time | O(n) space
class Solution1:
    def kthSmallest(self, root, k):
        values = []
        self.compute_first_k_values(root, k, values)
        return values[k - 1]

    def compute_first_k_values(self, root, k, values):
        if not root:
            return
        self.compute_first_k_values(root.left, k, values)
        values.append(root.val)
        self.compute_first_k_values(root.right, k, values)


# O(h) time | O(h) space
# a preferred way since it has early stopping
class Solution2:
    def kthSmallest(self, root, k):
        n = 0
        curr = root
        stack = [curr]
        while stack:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            n += 1
            if n == k:
                return curr.val
            curr = curr.right


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.left.right = TreeNode(2)

    solutions = [Solution1(), Solution2()]
    for solution in solutions:
        assert solution.kthSmallest(root, 1) == 1
        assert solution.kthSmallest(root, 2) == 2
        assert solution.kthSmallest(root, 3) == 3
        assert solution.kthSmallest(root, 4) == 4
