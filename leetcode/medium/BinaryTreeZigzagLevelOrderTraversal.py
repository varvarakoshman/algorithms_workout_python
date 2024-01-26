# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# O(n) time | O(n) space
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result = []
        is_left_to_right = True
        queue = [root]
        while queue:
            level_size = len(queue)
            level_nodes = [0] * level_size
            insert_idx = 0 if is_left_to_right else level_size - 1
            for _ in range(level_size):
                node = queue.pop(0)
                level_nodes[insert_idx] = node.val
                if is_left_to_right:
                    insert_idx += 1
                else:
                    insert_idx -= 1
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            is_left_to_right = not is_left_to_right
            result.append(level_nodes)
        return result
