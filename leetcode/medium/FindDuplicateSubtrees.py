class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# O(n^2) time | O(n^2) space
class Solution1:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        if not root:
            return []
        return self.get_repeating_nodes_with_bfs(root)

    def get_repeating_nodes_with_bfs(self, root):
        repeating_nodes = []
        subtrees_representations_with_count = {}
        queue = [root]
        while queue:
            level_count = len(queue)
            for _ in range(level_count):
                node = queue.pop(0)
                curr_repr = ''.join(self.get_subtree_preorder_representation(node, []))
                if curr_repr not in subtrees_representations_with_count:
                    subtrees_representations_with_count[curr_repr] = 1
                else:
                    subtrees_representations_with_count[curr_repr] += 1
                if subtrees_representations_with_count[curr_repr] == 2:
                    repeating_nodes.append(node)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return repeating_nodes

    def get_subtree_preorder_representation(self, node, subtree_values):
        if not node:
            subtree_values.append('')
            return subtree_values
        subtree_values.append('(')
        self.get_subtree_preorder_representation(node.left, subtree_values)
        subtree_values.append(')')
        subtree_values.append(str(node.val))
        subtree_values.append('(')
        self.get_subtree_preorder_representation(node.right, subtree_values)
        subtree_values.append(')')
        return subtree_values

# O(n) time | O(n) space
class Solution2:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        if not root:
            return []
        return self.get_repeating_nodes_with_bfs(root)

    def get_repeating_nodes_with_bfs(self, root):
        repeating_nodes = []
        subtrees_representations_with_count = {}
        representation_mapping = {}
        queue = deque()
        queue.append(root)
        while queue:
            level_count = len(queue)
            for _ in range(level_count):
                node = queue.popleft()
                curr_repr = self.get_subtree_postorder_representation(node, representation_mapping)
                if curr_repr not in subtrees_representations_with_count:
                    subtrees_representations_with_count[curr_repr] = 1
                else:
                    subtrees_representations_with_count[curr_repr] += 1
                if subtrees_representations_with_count[curr_repr] == 2:
                    repeating_nodes.append(node)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return repeating_nodes

    def get_subtree_postorder_representation(self, node, representation_mapping):
        if not node:
            return None
        left_id = self.get_subtree_postorder_representation(node.left, representation_mapping)
        right_id = self.get_subtree_postorder_representation(node.right, representation_mapping)
        curr_tripplet = tuple([left_id, node.val, right_id])
        if curr_tripplet in representation_mapping:
            return representation_mapping[curr_tripplet]
        new_id = len(representation_mapping) + 1
        representation_mapping[curr_tripplet] = new_id
        return new_id
