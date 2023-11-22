# O(n) time | O(1) space
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m = len(needle)
        n = len(haystack)
        for window_start in range(n - m + 1):
            for i in range(m):
                if needle[i] != haystack[window_start + i]:
                    break
                if i == m - 1:
                    return window_start
        return -1


if __name__ == '__main__':
    solution = Solution()
    assert solution.strStr("sadbutsad", "sad") == 0
    assert solution.strStr("sad", "sadbut") == -1
    assert solution.strStr("sadbutsad", "but") == 3
    assert solution.strStr("badbutsad", "sad") == 6
    assert solution.strStr("leetcode", "leeto") == -1
    assert solution.strStr("leetcodeleeto", "leeto") == 8
    assert solution.strStr("mississippi", "issip") == 4
    assert solution.strStr("aabaaabaaac", "aabaaac") == 4
