class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


# O(n) time | O(n) space
class Solution(object):
    def copyRandomList(self, head):
        nodes_mapping = {None: None}
        curr_node = head
        while curr_node:
            new_node = Node(curr_node.val)
            nodes_mapping[curr_node] = new_node
            curr_node = curr_node.next
        curr_node = head
        while curr_node:
            new_node = nodes_mapping[curr_node]
            new_node.next = nodes_mapping[curr_node.next]
            new_node.random = nodes_mapping[curr_node.random]
            curr_node = curr_node.next
        return nodes_mapping[head]
