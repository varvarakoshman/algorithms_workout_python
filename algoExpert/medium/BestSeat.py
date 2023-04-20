import unittest


# O(n) time | O(1) space
def bestSeat(seats):
    start_idx, optimal_idx = -1, -1
    max_space = 0
    curr_idx = 0
    while curr_idx < len(seats):
        if seats[curr_idx] != 0 and start_idx != -1:
            available_space = curr_idx - start_idx
            if available_space > max_space:
                max_space = available_space
                middle = (curr_idx - start_idx) // 2
                optimal_idx = start_idx + middle if available_space % 2 == 1 else start_idx + middle - 1
            start_idx = -1
        elif seats[curr_idx] == 0 and start_idx == -1:
            start_idx = curr_idx
        curr_idx += 1
    return optimal_idx


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = [1, 0, 1, 0, 0, 0, 1]
        expected = 4
        actual = bestSeat(input)
        self.assertEqual(actual, expected)

    def test_case_2(self):
        input = [1, 0, 0, 1]
        expected = 1
        actual = bestSeat(input)
        self.assertEqual(actual, expected)

    def test_case_3(self):
        input = [1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1]
        expected = 3
        actual = bestSeat(input)
        self.assertEqual(actual, expected)
