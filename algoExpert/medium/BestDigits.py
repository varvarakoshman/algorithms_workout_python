import unittest


# O(n) time | O(n) space
def bestDigits(number, num_digits):
    stack = [number[0]]
    for i in range(1, len(number)):
        while num_digits > 0 and len(stack) > 0 and number[i] > stack[-1]:
            num_digits -= 1
            stack.pop()
        stack.append(number[i])
    while num_digits > 0:
        num_digits -= 1
        stack.pop()
    return ''.join(stack)


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        number = "462839"
        numDigits = 2
        expected = "6839"
        actual = bestDigits(number, numDigits)
        self.assertEqual(actual, expected)

    def test_case_2(self):
        number = "462839"
        numDigits = 3
        expected = "839"
        actual = bestDigits(number, numDigits)
        self.assertEqual(actual, expected)

    def test_case_3(self):
        number = "12345"
        numDigits = 2
        expected = "345"
        actual = bestDigits(number, numDigits)
        self.assertEqual(actual, expected)

    def test_case_4(self):
        number = "11111"
        numDigits = 2
        expected = "111"
        actual = bestDigits(number, numDigits)
        self.assertEqual(actual, expected)

    def test_case_5(self):
        number = "129847563"
        numDigits = 4
        expected = "98763"
        actual = bestDigits(number, numDigits)
        self.assertEqual(actual, expected)

    def test_case_6(self):
        number = "4621111"
        numDigits = 4
        expected = "621"
        actual = bestDigits(number, numDigits)
        self.assertEqual(actual, expected)

    def test_case_7(self):
        number = "321"
        numDigits = 1
        expected = "32"
        actual = bestDigits(number, numDigits)
        self.assertEqual(actual, expected)