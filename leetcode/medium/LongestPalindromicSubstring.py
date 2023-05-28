# O(n^2) time | O(n) space
class Solution:
    def longestPalindrome(self, s):
        longest_so_far = s[0]
        for i in range(1, len(s)):
            even_palindrome = self.get_palindrome_length(s, i - 1, i)
            odd_palindrome = self.get_palindrome_length(s, i - 1, i + 1)
            curr_longest = even_palindrome if len(even_palindrome) > len(odd_palindrome) else odd_palindrome
            if len(curr_longest) > len(longest_so_far):
                longest_so_far = curr_longest
        return longest_so_far

    def get_palindrome_length(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]


if __name__ == '__main__':
    solution = Solution()
    assert solution.longestPalindrome("babad") == "bab"
    assert solution.longestPalindrome("cbbd") == "bb"
    assert solution.longestPalindrome("abcdcbakk") == "abcdcba"
    assert solution.longestPalindrome("kkabcdcba") == "abcdcba"
    assert solution.longestPalindrome("abbakdfff") == "abba"
    assert solution.longestPalindrome("abbacab") == "bacab"
    assert solution.longestPalindrome("bacabba") == "bacab"
    assert solution.longestPalindrome("aaa") == "aaa"
    assert solution.longestPalindrome("aaaa") == "aaaa"
    assert solution.longestPalindrome("aa") == "aa"
    assert solution.longestPalindrome("a") == "a"
