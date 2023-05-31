# Recursive approach with memoization
# O(n) time | O(n) space
class Solution1:
    def numDecodings(self, s):
        memoization = [-1] * len(s)
        return self.numDecodings_helper(s, 0, memoization)

    def numDecodings_helper(self, s, index, memoization):
        if index == len(s):
            return 1
        single = int(s[index])
        if single == 0:
            return 0
        if memoization[index] != -1:
            return memoization[index]
        curr_count = 0
        if 1 <= single <= 9:
            curr_count += self.numDecodings_helper(s, index + 1, memoization)
        if index < len(s) - 1 and 1 <= int(s[index:index + 2]) <= 26:
            curr_count += self.numDecodings_helper(s, index + 2, memoization)
        memoization[index] = curr_count
        return curr_count


# DP-1 approach
# Same complexity: O(n) time | O(n) space
class Solution2:
    def numDecodings(self, s):
        dp = [-1] * (len(s) + 1)
        dp[len(s)] = 1
        for i in range(len(s) - 1, -1, -1):
            dp[i] = dp[i + 1] if s[i] != '0' else 0
            if i + 1 < len(s) and (s[i] == '1' or s[i] == '2' and 0 <= int(s[i + 1]) < 7):
                dp[i] += dp[i + 2]
        return dp[0]


# DP-1 approach - storing only 2 latest values
# Optimal complexity: O(n) time | O(1) space
class Solution3:
    def numDecodings(self, s):
        prev, prev_prev = 1, -1
        for i in range(len(s) - 1, -1, -1):
            curr_count = prev if s[i] != '0' else 0
            if i + 1 < len(s) and (s[i] == '1' or s[i] == '2' and 0 <= int(s[i + 1]) < 7):
                curr_count += prev_prev
            prev_prev = prev
            prev = curr_count
        return prev


if __name__ == '__main__':
    solutions = [Solution1(), Solution2(), Solution3()]
    for solution in solutions:
        assert solution.numDecodings("11106") == 2
        assert solution.numDecodings("12") == 2
        assert solution.numDecodings("226") == 3
        assert solution.numDecodings("06") == 0
        assert solution.numDecodings("11106") == 2
        assert solution.numDecodings("12203") == 2
