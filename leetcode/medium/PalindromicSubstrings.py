# O(n^2) time | O(1) space
class Solution:
    def countSubstrings(self, s):
        count = 1
        for i in range(1, len(s)):
            count += 1
            count += self.get_palindrome_count(s, i - 1, i)
            count += self.get_palindrome_count(s, i - 1, i + 1)
        return count

    def get_palindrome_count(self, s, left, right):
        count = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1
        return count


if __name__ == '__main__':
    solution = Solution()
    assert solution.countSubstrings("abc") == 3
    assert solution.countSubstrings("aaa") == 6
