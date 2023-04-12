# This is an input class. Do not edit.
import unittest


class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# Solution 1
# O(n + m) time | O(1) space
def mergingLinkedLists_0(linked_list_one, linked_list_two):
    length_one = get_linked_list_length(linked_list_one)
    length_two = get_linked_list_length(linked_list_two)
    if length_one > length_two:
        linked_list_one = move_forward(linked_list_one, length_one - length_two)
    elif length_two > length_one:
        linked_list_two = move_forward(linked_list_two, length_two - length_one)
    return get_merging_point(linked_list_one, linked_list_two)


def get_linked_list_length(linked_list):
    curr_node = linked_list
    length = 0
    while curr_node is not None:
        length += 1
        curr_node = curr_node.next
    return length


def move_forward(linked_list, distance):
    for _ in range(distance):
        linked_list = linked_list.next
    return linked_list


def get_merging_point(linked_list_one, linked_list_two):
    merging_point = None
    while linked_list_one is not None:
        if linked_list_one.value == linked_list_two.value and merging_point is None:
            merging_point = linked_list_one
        elif linked_list_one.value != linked_list_two.value and merging_point is not None:
            return None
        linked_list_one = linked_list_one.next
        linked_list_two = linked_list_two.next
    return merging_point


# Intuition:
# 1 -------  len-2
#          \
#           *--------- len-3
# 2    ----/ len-1
# the path to merging point (*) for each list can be constructed as follows:
# path 1 to * = len-2 + len-3 + len-1
# path 2 to * = len-1 + len-3 + len-2
# => so pointers will meet at the merging point in 3 passes (instead of 4 in the solution 1)

# Solution 2
# O(n + m) time | O(1) space
def mergingLinkedLists(linked_list_one, linked_list_two):
    curr_node_one = linked_list_one
    curr_node_two = linked_list_two
    while curr_node_one is not curr_node_two:
        if curr_node_one is None:
            curr_node_one = linked_list_two
        else:
            curr_node_one = curr_node_one.next

        if curr_node_two is None:
            curr_node_two = linked_list_one
        else:
            curr_node_two = curr_node_two.next
    return curr_node_one


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        l1 = LinkedList(1)
        l1.next = LinkedList(2)
        l2 = LinkedList(3)
        l2.next = l1.next

        expected = l1.next
        actual = mergingLinkedLists(l1, l2)
        self.assertEqual(actual, expected)

    def test_case_2(self):
        l1 = LinkedList(2)
        l1.next = LinkedList(3)
        l1.next.next = LinkedList(1)
        l1.next.next.next = LinkedList(4)
        l2 = LinkedList(7)
        l2.next = l1.next.next
        l2.next.next = l1.next.next.next

        expected = l1.next.next
        actual = mergingLinkedLists(l1, l2)
        self.assertEqual(actual, expected)
