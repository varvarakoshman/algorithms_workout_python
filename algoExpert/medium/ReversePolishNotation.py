import unittest


# O(n) time | O(n) space
def reversePolishNotation(tokens):
    operators = ['+', '-', '*', '/']
    operation_stack = []
    for token in tokens:
        if token in operators:
            first_value = operation_stack.pop()
            second_value = operation_stack.pop()
            result = apply_operator(first_value, second_value, token)
            operation_stack.append(result)
        else:
            operation_stack.append(int(token))
    return operation_stack.pop()


def apply_operator(first_value, second_value, operator):
    if operator == '+':
        return second_value + first_value
    elif operator == '-':
        return second_value - first_value
    elif operator == '*':
        return second_value * first_value
    else:
        return int(second_value / first_value)  # ! ROUNDING TOWARDS ZERO


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = ["3", "2", "+", "7", "*"]
        expected = 35
        actual = reversePolishNotation(input)
        self.assertEqual(actual, expected)

    def test_case_2(self):
        input = ["-50", "3", "17", "+", "2", "-", "/"]
        expected = -2
        actual = reversePolishNotation(input)
        self.assertEqual(actual, expected)
