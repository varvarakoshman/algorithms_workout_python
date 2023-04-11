# Do not edit the class below except for the
# populateSuffixTrieFrom and contains methods.
# Feel free to add new properties and methods
# to the class.
import unittest


class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = "*"
        self.populateSuffixTrieFrom(string)

    # O(n^2) time | O(n^2) space
    def populateSuffixTrieFrom(self, string):
        for start_idx in range(len(string)):
            self.insert_substring_starting_at(start_idx, string)

    def insert_substring_starting_at(self, start_idx, string):
        curr_node = self.root
        for char_idx in range(start_idx, len(string)):
            character = string[char_idx]
            if character not in curr_node.keys():
                curr_node[character] = {}
            curr_node = curr_node[character]
        curr_node[self.endSymbol] = True

    #  O(m) time | O(1) space, m - length of the string
    def contains(self, string):
        curr_node = self.root
        for character in string:
            if character not in curr_node.keys():
                return False
            curr_node = curr_node[character]
        return self.endSymbol in curr_node


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        trie = SuffixTrie("babc")
        expected = {
            "c": {"*": True},
            "b": {"c": {"*": True}, "a": {"b": {"c": {"*": True}}}},
            "a": {"b": {"c": {"*": True}}},
        }
        self.assertEqual(trie.root, expected)
        self.assertTrue(trie.contains("abc"))