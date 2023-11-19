# O(n) time | O(1) space
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        curr_idx = len(s) - 1
        while curr_idx >= 0:
            if s[curr_idx] != ' ':
                count += 1
            elif count > 0:
                return count
            curr_idx -= 1
        return count


if __name__ == '__main__':
    solution = Solution()
    assert solution.lengthOfLastWord("Hello World") == 5
    assert solution.lengthOfLastWord("   fly me   to   the moon  ") == 4
    assert solution.lengthOfLastWord("luffy is still joyboy") == 6
