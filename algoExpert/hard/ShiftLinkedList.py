import unittest


class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# O(n) time | O(1) space
def shiftLinkedList(head, k):
    list_size = get_list_size(head)
    shift = abs(k) % list_size
    if shift == 0:
        return head
    if k > 0:
        return shift_right(head, shift)
    elif k < 0:
        return shift_left(head, shift)


def shift_right(head, shift):
    left_pointer, right_pointer = head, head
    for i in range(shift):
        right_pointer = right_pointer.next
    while right_pointer.next is not None:
        left_pointer = left_pointer.next
        right_pointer = right_pointer.next
    new_head = left_pointer.next
    left_pointer.next = None
    right_pointer.next = head
    return new_head


def shift_left(head, shift):
    left_pointer = head
    for i in range(shift - 1):
        left_pointer = left_pointer.next
    new_head = left_pointer.next
    right_pointer = new_head
    left_pointer.next = None
    while right_pointer.next is not None:
        right_pointer = right_pointer.next
    right_pointer.next = head
    return new_head


def get_list_size(head):
    size = 0
    while head is not None:
        size += 1
        head = head.next
    return size


def linkedListToArray(head):
    array = []
    current = head
    while current is not None:
        array.append(current.value)
        current = current.next
    return array


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        head = LinkedList(0)
        head.next = LinkedList(1)
        head.next.next = LinkedList(2)
        head.next.next.next = LinkedList(3)
        head.next.next.next.next = LinkedList(4)
        head.next.next.next.next.next = LinkedList(5)
        result = shiftLinkedList(head, 2)
        array = linkedListToArray(result)

        expected = [4, 5, 0, 1, 2, 3]
        self.assertEqual(expected, array)

    def test_case_2(self):
        head = LinkedList(0)
        head.next = LinkedList(1)
        head.next.next = LinkedList(2)
        head.next.next.next = LinkedList(3)
        head.next.next.next.next = LinkedList(4)
        head.next.next.next.next.next = LinkedList(5)
        result = shiftLinkedList(head, -2)
        array = linkedListToArray(result)

        expected = [2, 3, 4, 5, 0, 1]
        self.assertEqual(expected, array)
