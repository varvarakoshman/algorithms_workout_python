import unittest


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# O(n) time | O(1) space
class Solution(object):
    def reorderList(self, head):
        middle = self.find_middle(head)
        right = self.reverse_list(middle)
        left = head
        while right.next:
            old_next_left, old_next_right = left.next, right.next
            left.next = right
            right.next = old_next_left

            left = old_next_left
            right = old_next_right

    def reverse_list(self, head):
        left = head
        prev = None
        while left:
            tmp = left.next
            left.next = prev
            prev = left
            left = tmp
        return prev

    def find_middle(self, head):
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        solution = Solution()
        # 1 -> 2 -> 3 -> 4 -> 5
        # 1 -> 2 -> 3 <- 4 <- 5
        # 1 -> 5 -> 2 -> 4 -> 3
        # [1, 2, 3, 4, 5]
        # =>
        # [1, 5, 2, 4, 3]
        input = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        expected = ListNode(1, ListNode(5, ListNode(2, ListNode(4, ListNode(3)))))
        actual = solution.reorderList(input)
        self.assertEqual(expected, actual)

    def test_case_2(self):
        solution = Solution()
        # [1, 2, 3, 4]
        # 1 -> 2 -> 3 -> 4
        # 1 -> 2 <- 3 <- 4
        # [1, 4, 2, 3]
        input = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
        expected = ListNode(1, ListNode(4, ListNode(2, ListNode(3))))
        actual = solution.reorderList(input)
        self.assertEqual(expected, actual)

    def test_case_3(self):
        solution = Solution()
        # [1, 2]
        # 1 -> 2
        # 1 -> 2
        # [2, 1]
        input = ListNode(1, ListNode(2))
        expected = ListNode(1, ListNode(2))
        actual = solution.reorderList(input)
        self.assertEqual(expected, actual)
