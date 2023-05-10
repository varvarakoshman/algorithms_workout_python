# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# O(n) time | O(n) space
class Solution:
    def levelOrder(self, root):
        result = []
        queue = collections.deque()
        queue.append(root)
        while len(queue) > 0:
            curr_level_num = len(queue)
            curr_level = []
            for _ in range(curr_level_num):
                curr_elem = queue.popleft()
                if curr_elem:
                    curr_level.append(curr_elem.val)
                    queue.append(curr_elem.left)
                    queue.append(curr_elem.right)
            if curr_level:
                result.append(curr_level)
        return result


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    assert Solution().levelOrder(root) == [[3], [9, 20], [15, 7]]

    root = TreeNode(1)
    assert Solution().levelOrder(root) == [[1]]

    assert Solution().levelOrder(None) == []
