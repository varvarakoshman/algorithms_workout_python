import unittest
from collections import defaultdict


# O(n*m) time | O(n) space, n - number of words, m - length of the longest word
def groupAnagrams(words):
    letter_frequencies = defaultdict(list)
    for word in words:
        letters_count = [0] * 26
        for letter in word:
            letters_count[ord(letter) - ord("a")] += 1
        letter_frequencies[tuple(letters_count)].append(word)
    return list(letter_frequencies.values())


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = ["eat", "tea", "tan", "ate", "nat", "bat"]
        expected = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
        actual = groupAnagrams(input)
        self.assertEqual(len(expected), len(actual))

    def test_case_2(self):
        self.assertEqual([[""]], groupAnagrams([""]))

    def test_case_3(self):
        self.assertEqual([["a"]], groupAnagrams(["a"]))
