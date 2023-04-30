class Solution(object):
    # O(26*n) ~ O(n) time | O(1) space
    def checkInclusion(self, s1, s2):
        s1_frequencies = self.get_frequencies(s1)
        left_pointer = 0
        curr_frequencies = {}
        for right_pointer in range(len(s2)):
            curr_letter = s2[right_pointer]
            if curr_frequencies == s1_frequencies:
                return True
            if curr_letter not in s1_frequencies:
                left_pointer = right_pointer + 1
                curr_frequencies = {}
            else:
                curr_frequencies[curr_letter] = curr_frequencies.get(curr_letter, 0) + 1
                if curr_frequencies[curr_letter] <= s1_frequencies[curr_letter]:
                    continue
                else:
                    while curr_frequencies[curr_letter] != s1_frequencies[curr_letter]:
                        self.shift_left_letter(curr_frequencies, s2[left_pointer])
                        left_pointer += 1
        return curr_frequencies == s1_frequencies

    def get_frequencies(self, string):
        frequencies = {}
        for letter in string:
            frequencies[letter] = frequencies.get(letter, 0) + 1
        return frequencies

    def shift_left_letter(self, curr_frequencies, letter):
        if curr_frequencies[letter] == 1:
            del curr_frequencies[letter]
        else:
            curr_frequencies[letter] -= 1


if __name__ == '__main__':
    assert Solution().checkInclusion("adc", "dcda") is True
    assert Solution().checkInclusion("ab", "eidbaooo") is True
    assert Solution().checkInclusion("ab", "eidboaoo") is False
    assert Solution().checkInclusion("abc", "cbaa") is True
    assert Solution().checkInclusion("abcc", "cbaabcc") is True
    assert Solution().checkInclusion("abc", "cba") is True
    assert Solution().checkInclusion("abc", "cbpaa") is False
    assert Solution().checkInclusion("a", "cbpaa") is True
    assert Solution().checkInclusion("a", "a") is True
