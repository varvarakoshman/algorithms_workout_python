import unittest


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    # 1 - 2 - 3
    # 4 - 5

    # 1 - 2 - 9
    # 4 - 5 - 6

    # 8 - 12
    # 2 - 4 - 9

    # 1 - 2 - 4
    # 1 - 3 - 4

    # 1
    # 3
    def mergeTwoLists(self, list1, list2):
        dummy_node = ListNode()
        prev = dummy_node
        while list1 and list2:
            if list1.val < list2.val:
                prev.next = list1
                list1 = list1.next
            else:
                prev.next = list2
                list2 = list2.next
            prev = prev.next
        if not list1 and list2:
            prev.next = list2
        elif list1 and not list2:
            prev.next = list1
        return dummy_node.next


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        l1 = ListNode(1)
        l1.next = ListNode(2)
        l1.next.next = ListNode(4)
        l2 = ListNode(1)
        l2.next = ListNode(3)
        l2.next.next = ListNode(4)

        actual = Solution().mergeTwoLists(l1, l2)


    def test_case_2(self):
        l1 = ListNode(1)
        l1.next = ListNode(2)
        l1.next.next = ListNode(3)
        l1.next.next.next = ListNode(4)
        l2 = ListNode(5)
        l2.next = ListNode(6)

        actual = Solution().mergeTwoLists(l1, l2)

