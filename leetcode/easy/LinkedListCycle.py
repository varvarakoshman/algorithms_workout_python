class Solution(object):

    # O(n) time | O(1) space
    def hasCycle(self, head):
        slow, fast = head, head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
