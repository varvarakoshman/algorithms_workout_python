# This is an input class. Do not edit.
import unittest


class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# O(n) time | O(1) space
def middleNode(linkedList):
    slow_pointer = linkedList
    fast_pointer = linkedList
    while fast_pointer and fast_pointer.next:
        slow_pointer = slow_pointer.next
        fast_pointer = fast_pointer.next.next
    return slow_pointer


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        linkedList = LinkedList(0)
        linkedList.next = LinkedList(1)
        expected = LinkedList(2)
        linkedList.next.next = expected
        expected.next = LinkedList(3)
        actual = middleNode(linkedList)
        self.assertEqual(actual, expected)
