# Recursive approach (brute force)
# O(n^2*m) time | O(n^2*m) space
# class Solution:
#     def wordBreak(self, s, wordDict):
#         unique_words = set(wordDict)
#
#         def word_break_helper(start):
#             if start == -1:
#                 return True
#             is_breakable = False
#             for i in range(start, -1, -1):
#                 if s[i: start + 1] in unique_words:
#                     is_breakable = is_breakable or word_break_helper(i - 1)
#             return is_breakable
#
#         return word_break_helper(len(s) - 1)

# DP-1 approach
# O(n^2*m) time | O(n) space
class Solution:
    def wordBreak(self, s, word_dict):
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for start in range(len(s) - 1, -1, -1):
            for dict_word in word_dict:
                right = start + len(dict_word)
                if right <= len(s) and s[start:right] == dict_word:
                    dp[start] = dp[right]
                if dp[start]:
                    break

        return dp[0]


if __name__ == '__main__':
    solution = Solution()
    assert solution.wordBreak("leetcode", ["leet", "code"]) is True
    assert solution.wordBreak("applepenapple", ["apple", "pen"]) is True
    assert solution.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]) is False
    assert solution.wordBreak("penpineapple", ["apple", "pen", "pineapple"]) is True
    assert solution.wordBreak("abcd", ["a", "abc", "b", "cd"]) is True
    assert solution.wordBreak("aebbbbs", ["a", "aeb", "ebbbb", "s", "eb"]) is True
