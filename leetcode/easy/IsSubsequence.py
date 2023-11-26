# O(max(n, m)) time | O(1) space
# n - text's length, m - substring's length
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        substring_pointer, text_pointer = 0, 0
        match_count = 0
        while substring_pointer < len(s) and text_pointer < len(t):
            if t[text_pointer] == s[substring_pointer]:
                substring_pointer += 1
                match_count += 1
            text_pointer += 1
        return match_count == len(s)


if __name__ == '__main__':
    solution = Solution()
    assert solution.isSubsequence("hgd", "ahbgdc") is True
    assert solution.isSubsequence("abc", "ahbgdc") is True
    assert solution.isSubsequence("agb", "ahbgdc") is False
    assert solution.isSubsequence("axc", "ahbgdc") is False
    assert solution.isSubsequence("abc", "abc") is True
    assert solution.isSubsequence("abc", "ab") is False
    assert solution.isSubsequence("a", "aaa") is True
    assert solution.isSubsequence("a", "a") is True
    assert solution.isSubsequence("", "abc") is True
    assert solution.isSubsequence("", "") is True
    assert solution.isSubsequence("abc", "") is False
