# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# O(n) time | O(n) space
class Solution:
    def rightSideView(self, root):
        result, stack = [], []
        if root:
            stack.append([root, 1])
        while stack:
            top_vertex, top_height = stack.pop()
            if top_height > len(result):
                result.append(top_vertex.val)
            if top_vertex.left:
                stack.append([top_vertex.left, top_height + 1])
            if top_vertex.right:
                stack.append([top_vertex.right, top_height + 1])
        return result


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.right = TreeNode(4)
    root.left.right = TreeNode(5)

    assert Solution().rightSideView(root) == [1, 3, 4]
