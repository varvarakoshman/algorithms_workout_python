# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# O(logn) time | O(logn) space
class Solution:
    def isValidBST(self, root):
        min_value = -float('inf')
        max_value = -min_value
        return self.validate_bst_helper(root, min_value, max_value)

    def validate_bst_helper(self, root, min_value, max_value):
        if not root:
            return True
        if root.val >= max_value or root.val <= min_value:
            return False
        return self.validate_bst_helper(root.left, min_value, root.val) and \
               self.validate_bst_helper(root.right, root.val, max_value)
