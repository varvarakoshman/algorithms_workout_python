import unittest


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# O(n) time | O(1) space
class Solution(object):
    def reverseList(self, head):
        prev = None
        while head:
            old_next = head.next
            head.next = prev
            prev = head
            head = old_next
        return prev


class TestProgram(unittest.TestCase):
    # 1 -> 2 -> 3 -> 4 -> 5
    # 1 <- 2 <- 3 <- 4 <- 5
    def test_case_1(self):
        solution = Solution()
        input = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        expected = ListNode(5, ListNode(4, ListNode(3, ListNode(2, ListNode(1)))))
        actual = solution.reverseList(input)
        # self.assertEqual(expected, actual)
