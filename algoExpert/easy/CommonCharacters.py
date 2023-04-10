import unittest


# O(n*m) time | O(m) space, n - number of strings, m - length of the longest string
def commonCharacters(strings):
    commons_chars = set(strings[0])
    for i in range(1, len(strings)):
        curr_unique = set()
        for char in strings[i]:
            if char in commons_chars:
                curr_unique.add(char)
        commons_chars = curr_unique
    return list(commons_chars)


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = ["abc", "bcd", "cbad"]
        expected = ["b", "c"]
        actual = commonCharacters(input)
        actual.sort()
        self.assertEqual(actual, expected)
