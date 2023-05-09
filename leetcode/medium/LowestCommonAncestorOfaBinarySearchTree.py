# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# O(logn) time | O(1) space
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        curr_node = root
        while curr_node:
            if p.val <= curr_node.val <= q.val or q.val <= curr_node.val <= p.val:
                break
            if p.val <= curr_node.val and q.val <= curr_node.val:
                curr_node = curr_node.left
            else:
                curr_node = curr_node.right
        return curr_node
