import unittest


class MinMaxStack:
    def __init__(self):
        self.stack = []
        self.min_values = []
        self.max_values = []

    # O(1) time | O(1) space
    def peek(self):
        return self.stack[-1] if len(self.stack) > 0 else None

    # O(1) time | O(1) space
    def pop(self):
        last_value = self.peek()
        if last_value is not None:
            del self.stack[-1]
            if last_value == self.min_values[-1]:
                del self.min_values[-1]
            if last_value == self.max_values[-1]:
                del self.max_values[-1]
        return last_value

    # O(1) time | O(1) space
    def push(self, number):
        self.stack.append(number)
        if len(self.max_values) == 0 or number >= self.max_values[-1]:
            self.max_values.append(number)
        if len(self.min_values) == 0 or number <= self.min_values[-1]:
            self.min_values.append(number)

    # O(1) time | O(1) space
    def getMin(self):
        return self.min_values[-1] if len(self.min_values) > 0 else None

    # O(1) time | O(1) space
    def getMax(self):
        return self.max_values[-1] if len(self.max_values) > 0 else None


def testMinMaxPeek(self, min, max, peek, stack):
    self.assertEqual(stack.getMin(), min)
    self.assertEqual(stack.getMax(), max)
    self.assertEqual(stack.peek(), peek)


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        stack = MinMaxStack()
        stack.push(5)
        testMinMaxPeek(self, 5, 5, 5, stack)
        stack.push(7)
        testMinMaxPeek(self, 5, 7, 7, stack)
        stack.push(2)
        testMinMaxPeek(self, 2, 7, 2, stack)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.pop(), 7)
        testMinMaxPeek(self, 5, 5, 5, stack)
