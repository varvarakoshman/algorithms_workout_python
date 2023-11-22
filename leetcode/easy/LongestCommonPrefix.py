from typing import (
    List,
)


# O(n*m) time | O(k) space
# n - number of words
# m - length of the longest word
# k - length of the common prefix
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        for index in range(len(strs[0])):
            curr_char = strs[0][index]
            for i in range(1, len(strs)):
                string = strs[i]
                if index >= len(string) or string[index] != curr_char:
                    return result
            result += curr_char
        return result


if __name__ == '__main__':
    solution = Solution()
    assert solution.longestCommonPrefix(["flower", "flow", "flight"]) == "fl"
    assert solution.longestCommonPrefix(["dog", "racecar", "car"]) == ""
    assert solution.longestCommonPrefix(["ab", "a"]) == "a"
