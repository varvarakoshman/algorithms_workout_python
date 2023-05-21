# O(n*2^n) time | O(n) space
class Solution1:
    def partition(self, s):
        result = []
        self.generate_partitions(s, [], 0, result)
        return result

    def generate_partitions(self, s, curr, start, result):
        if start == len(s):
            result.append(curr[:])
            return
        for end in range(start, len(s)):
            substring = s[start:end + 1]
            if self.is_palindrome(substring):
                curr.append(substring)
                self.generate_partitions(s, curr, end + 1, result)
                curr.pop()

    def is_palindrome(self, substring):
        start, end = 0, len(substring) - 1
        while start < end:
            if substring[start] != substring[end]:
                return False
            start += 1
            end -= 1
        return True


# NB the longer input string => the longer is palindrome check for substrings
# dp can be used to store results of already checked substrings (solution 2)

# O(n*2^n) time | O(n^2) space
class Solution2:
    def partition(self, s):
        result = []
        dp = [[None for _ in range(len(s))] for _ in range(len(s))]
        self.generate_partitions(s, [], 0, dp, result)
        return result

    def generate_partitions(self, s, curr, start, dp, result):
        if start == len(s):
            result.append(curr[:])
            return
        for end in range(start, len(s)):
            substring = s[start:end + 1]
            if dp[start][end] is not None:
                is_palindrome = dp[start][end]
            else:
                is_palindrome = self.is_palindrome(substring)
                dp[start][end] = is_palindrome
            if is_palindrome:
                curr.append(substring)
                self.generate_partitions(s, curr, end + 1, dp, result)
                curr.pop()

    def is_palindrome(self, substring):
        start, end = 0, len(substring) - 1
        while start < end:
            if substring[start] != substring[end]:
                return False
            start += 1
            end -= 1
        return True


if __name__ == '__main__':
    # assert Solution1().partition("aab") == [["a", "a", "b"], ["aa", "b"]]
    assert Solution2().partition("aab") == [["a", "a", "b"], ["aa", "b"]]
