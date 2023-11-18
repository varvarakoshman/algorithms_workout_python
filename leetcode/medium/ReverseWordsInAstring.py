# O(n) time | O(n) space
class Solution:
    def reverseWords(self, s: str) -> str:
        words = []
        start_idx = 0
        for curr_idx in range(len(s)):
            if s[curr_idx] == " " and curr_idx - 1 >= 0 and s[curr_idx - 1] != " ":
                words.append(s[start_idx:curr_idx])
                start_idx = -1
            elif s[curr_idx] != " " and curr_idx - 1 >= 0 and s[curr_idx - 1] == " ":
                start_idx = curr_idx
        if start_idx != -1:
            words.append(s[start_idx:])
        words.reverse()
        return " ".join(words)


if __name__ == '__main__':
    solution = Solution()
    assert solution.reverseWords("the sky is blue") == "blue is sky the"
    assert solution.reverseWords("  hello world  ") == "world hello"
    assert solution.reverseWords("a good   example") == "example good a"
