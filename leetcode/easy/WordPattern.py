# O(n) time | O(n) space
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        letter_to_word_mapping = {}
        word_to_pattern_mapping = {}
        words = s.split()
        if len(pattern) != len(words):
            return False
        for i in range(len(pattern)):
            letter = pattern[i]
            word = words[i]
            if word in word_to_pattern_mapping or letter in letter_to_word_mapping:
                is_bijectional = self.check_bijection(letter, word, letter_to_word_mapping, word_to_pattern_mapping)
                if not is_bijectional:
                    return False
            else:
                letter_to_word_mapping[letter] = word
                word_to_pattern_mapping[word] = letter
        return True

    def check_bijection(self, first, second, first_mapping, second_mapping):
        return first in first_mapping and second in second_mapping \
            and first_mapping[first] == second and second_mapping[second] == first


if __name__ == '__main__':
    solution = Solution()
    assert solution.wordPattern("abba", "dog cat cat dog") is True
    assert solution.wordPattern("abba", "dog cat cat fish") is False
    assert solution.wordPattern("aaaa", "dog cat cat dog") is False
    assert solution.wordPattern("abba", "dog dog dog dog") is False
