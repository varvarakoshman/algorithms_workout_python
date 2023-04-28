import unittest


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# O(n) time | O(1) space
class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0, head)
        slow, fast = dummy, dummy
        for _ in range(n):
            fast = fast.next
        while fast.next:
            slow = slow.next
            fast = fast.next
        to_delete = slow.next
        slow.next = to_delete.next
        to_delete.next = None
        return dummy.next


class TestProgram(unittest.TestCase):
    #  x -> 1 -> 2 -> 3 -> 4 -> 5, 2
    # 1 -> 2 -> 3 -> 5
    def test_case_1(self):
        solution = Solution()
        input = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        expected = ListNode(1, ListNode(2, ListNode(3, ListNode(5))))
        actual = solution.removeNthFromEnd(input, 1)
