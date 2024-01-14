# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# recursive
# O(n) time | O(n) space
class Solutio1:

    def __init__(self):
        self.lowest_common_ancestor = None

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.is_target_node(root, p, q)
        return self.lowest_common_ancestor

    def is_target_node(self, node, p, q):
        if not node:
            return False

        is_middle = node.val == p.val or node.val == q.val
        is_in_left = self.is_target_node(node.left, p, q)
        is_in_right = self.is_target_node(node.right, p, q)

        if is_in_left and is_in_right or is_middle and (is_in_left or is_in_right):
            self.lowest_common_ancestor = node

        return is_middle or is_in_left or is_in_right


# iterative
# O(n) time | O(n) space
class Solution2:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ancestors_mapping_p = self.dfs(root, p)
        ancestors_p = self.get_ancestors(ancestors_mapping_p, p)
        ancestors_mapping_q = self.dfs(root, q)
        return self.find_lowest(q, ancestors_mapping_q, ancestors_p)

    def dfs(self, root, target):
        ancestors_mapping = {root: None}
        stack = [root]
        while stack:
            curr = stack.pop()
            if curr.val == target.val:
                break
            if curr.left:
                ancestors_mapping[curr.left] = curr
                stack.append(curr.left)
            if curr.right:
                ancestors_mapping[curr.right] = curr
                stack.append(curr.right)
        return ancestors_mapping

    def get_ancestors(self, ancestors_mapping, node):
        ancestors = set()
        curr = node
        while curr:
            ancestors.add(curr)
            curr = ancestors_mapping[curr]
        return ancestors

    def find_lowest(self, start_node, ancestors_mapping, other_ancestors):
        curr = start_node
        while curr not in other_ancestors:
            curr = ancestors_mapping[curr]
        return curr
