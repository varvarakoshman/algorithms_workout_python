import unittest


# O(n) time | O(1) space
def hasSingleCycle(array):
    num_elements_visited = 0
    curr_idx = 0
    while num_elements_visited < len(array):
        if num_elements_visited > 0 and curr_idx == 0:
            return False
        jump = array[curr_idx]
        num_elements_visited += 1
        curr_idx = (curr_idx + jump) % len(array)
    return curr_idx == 0


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(hasSingleCycle([2, 3, 1, -4, -4, 2]), True)
        self.assertEqual(hasSingleCycle([1, -1, 1, -1]), False)
        self.assertEqual(hasSingleCycle([5, 1, 1, -2, -4, -1]), False)
        self.assertEqual(hasSingleCycle([2, 3, 1, 2, 1, -4]), False)
        self.assertEqual(hasSingleCycle([2, 2, -1]), True)
        self.assertEqual(hasSingleCycle([1, 1, 1, 1, 1]), True)
        self.assertEqual(hasSingleCycle([1, 1, 0, 1, 1]), False)
        self.assertEqual(hasSingleCycle([0]), True)
