# O(1) time | O(1) space

# As there is a finite set of roman numerals, the maximum number possible number can be 3999,
# which in roman numerals is MMMCMXCIX. As such the time complexity is O(1).
class Solution:

    ROMAN_NUMBERS = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    def romanToInt(self, s: str) -> int:
        curr_idx = 0
        int_number = 0
        while curr_idx < len(s):
            curr_number = self.ROMAN_NUMBERS[s[curr_idx]]
            if curr_idx + 1 < len(s) and curr_number < self.ROMAN_NUMBERS[s[curr_idx + 1]]:
                int_number += (self.ROMAN_NUMBERS[s[curr_idx + 1]] - curr_number)
                curr_idx += 2
            else:
                int_number += curr_number
                curr_idx += 1
        return int_number


if __name__ == '__main__':
    solution = Solution()
    assert solution.romanToInt("III") == 3
    assert solution.romanToInt("LVIII") == 58
    assert solution.romanToInt("MCMXCIV") == 1994
