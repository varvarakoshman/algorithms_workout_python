# This is an input class. Do not edit.
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

    def getNodesInArray(self):
        nodes = []
        current = self
        while current is not None:
            nodes.append(current.value)
            current = current.next
        return nodes


# O(n + m) time | O(1) space
def mergeLinkedLists(headOne, headTwo):
    if headOne.value > headTwo.value:
        min_head = headTwo
        resulting_head = headTwo
        headTwo = headTwo.next
    else:
        min_head = headOne
        resulting_head = headOne
        headOne = headOne.next
    while headOne is not None and headTwo is not None:
        if headOne.value < headTwo.value:
            min_head.next = headOne
            min_head = headOne
            headOne = headOne.next
        else:
            min_head.next = headTwo
            min_head = headTwo
            headTwo = headTwo.next
    restNode = headTwo if headOne is None else headOne
    while restNode is not None:
        min_head.next = restNode
        min_head = restNode
        restNode = restNode.next
    return resulting_head


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        list1 = LinkedList(2).addMany([6, 7, 8])
        list2 = LinkedList(1).addMany([3, 4, 5, 9, 10])
        output = mergeLinkedLists(list1, list2)
        expectedNodes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(output.getNodesInArray(), expectedNodes)

    def test_case_2(self):
        list1 = LinkedList(5).addMany([6, 7, 8])
        list2 = LinkedList(1).addMany([3, 4, 9, 10])
        output = mergeLinkedLists(list1, list2)
        expectedNodes = [1, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(output.getNodesInArray(), expectedNodes)

    def test_case_3(self):
        list1 = LinkedList(1)
        list2 = LinkedList(1)
        output = mergeLinkedLists(list1, list2)
        expectedNodes = [1, 1]
        self.assertEqual(output.getNodesInArray(), expectedNodes)
