import unittest


# O(n * m) time | O(n * m) space
# n - number of words, m - length of the longest word
def semordnilap(words):
    all_reversed = set()
    result = []
    for word in words:
        # reverse = "".join([letter for letter in reversed(word)])
        reverse = word[::-1]
        if word in all_reversed:
            result.append([word, reverse])
            all_reversed.remove(word)
        else:
            all_reversed.add(reverse)
    return result


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(semordnilap(["desserts", "stressed", "hello"]), [["stressed", "desserts"]])
        self.assertEqual(semordnilap([]), [])
        self.assertEqual(semordnilap(["a", "b", "c"]), [])
        self.assertEqual(semordnilap(["bb", "aaa", "aaa", "bb"]), [["aaa", "aaa"], ["bb", "bb"]])
