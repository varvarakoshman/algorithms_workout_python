from typing import (
    List, Optional
)


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# O(n) time | O(n) space
class Solution:

    def __init__(self):
        self.curr_root_idx = 0

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def construct_tree(left, right):
            if left > right:
                return None
            curr_root_value = preorder[self.curr_root_idx]
            new_node = TreeNode(curr_root_value)
            self.curr_root_idx += 1
            middle_idx = node_to_idx_mapping[curr_root_value]
            new_node.left = construct_tree(left, middle_idx - 1)
            new_node.right = construct_tree(middle_idx + 1, right)
            return new_node

        node_to_idx_mapping = {elem: idx for idx, elem in enumerate(inorder)}
        return construct_tree(0, len(preorder) - 1)
