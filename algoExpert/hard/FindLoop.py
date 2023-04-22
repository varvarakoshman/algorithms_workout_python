import unittest


class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

    def addMany(self, values):
        current = self
        while current.next is not None:
            current = current.next
        for value in values:
            current.next = LinkedList(value)
            current = current.next
        return self

    def getNthNode(self, n):
        counter = 1
        current = self
        while counter < n:
            current = current.next
            counter += 1
        return current


# O(n) time | O(1) space
def findLoop(head):
    fast_pointer = head.next.next
    slow_pointer = head.next
    while fast_pointer != slow_pointer:
        fast_pointer = fast_pointer.next.next
        slow_pointer = slow_pointer.next
    slow_pointer = head
    while slow_pointer != fast_pointer:
        slow_pointer = slow_pointer.next
        fast_pointer = fast_pointer.next
    return slow_pointer


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        test = LinkedList(0).addMany([1, 2, 3, 4, 5, 6, 7, 8, 9])
        test.getNthNode(10).next = test.getNthNode(5)
        self.assertEqual(findLoop(test), test.getNthNode(5))
