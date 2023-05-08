# O(m*n) time | O(m) space, m=26 (English letters)
class Solution1(object):
    def characterReplacement(self, string, k):
        frequencies = {}
        longest_seq_len, left = 0, 0
        for right in range(len(string)):
            new_letter = string[right]
            frequencies[new_letter] = frequencies.get(new_letter, 0) + 1
            window_len = right - left + 1
            most_frequent_count = self.get_most_frequent(frequencies)
            k_allowed = window_len - most_frequent_count
            if k_allowed <= k:
                longest_seq_len = max(longest_seq_len, window_len)
            else:
                frequencies[string[left]] -= 1
                left += 1
        return longest_seq_len

    def get_most_frequent(self, frequencies):
        max_count = 0
        for _, value in frequencies.items():
            max_count = max(max_count, value)
        return max_count


# Optimized version of Solution 1 - without 26 passing on every iteration
# O(n) time | O(m) space, m=26 (English letters)
# explained https://leetcode.com/problems/longest-repeating-character-replacement/editorial/
class Solution1_1(object):
    def characterReplacement(self, string, k):
        frequencies = {}
        longest_seq_len, max_count = 0, 0
        left = 0
        for right in range(len(string)):
            new_letter = string[right]
            frequencies[new_letter] = frequencies.get(new_letter, 0) + 1
            max_count = max(max_count, frequencies[new_letter])

            window_len = right - left + 1
            is_window_valid = window_len - max_count <= k
            if is_window_valid:
                longest_seq_len = window_len
            else:
                frequencies[string[left]] -= 1
                left += 1
        return longest_seq_len


# O(26*n) time | O(1) space
class Solution2(object):
    def characterReplacement(self, s, k):
        unique_letters = set([letter for letter in s])
        max_len = 0
        for letter in unique_letters:
            edit_count, start_idx = 0, 0
            for i in range(len(s)):
                if s[i] == letter:
                    continue
                if edit_count < k:
                    edit_count += 1
                else:
                    max_len = max(max_len, i - start_idx)
                    while s[start_idx] == letter:
                        start_idx += 1
                    start_idx += 1
            max_len = max(max_len, len(s) - start_idx)
        return max_len


if __name__ == '__main__':
    solutions = [Solution1(), Solution1_1(), Solution2()]
    for solution in solutions:
        assert solution.characterReplacement("DAABACDDDD", 3) == 7
        assert solution.characterReplacement("DAABACAA", 3) == 8
        assert solution.characterReplacement("BAAAB", 2) == 5
        assert solution.characterReplacement("AABABBA", 1) == 4
        assert solution.characterReplacement("KRSCDCSONAJNHLBMDQGIFCPEKPOHQIHLTDIQGEKLRLCQNBOHNDQGHJPNDQPERNFSSSRDEQLFPCCCARFMDLHADJADAGNNSBNCJQOF", 4) == 7
        assert solution.characterReplacement("ABAA", 0) == 2
        assert solution.characterReplacement("ABAB", 2) == 4
        assert solution.characterReplacement("A", 1) == 1
        assert solution.characterReplacement("AABABBABB", 1) == 5
