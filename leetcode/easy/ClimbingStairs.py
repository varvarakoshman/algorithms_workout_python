# O(n) time | O(n) space
class Solution:
    def climbStairs(self, n):
        if n == 1:
            return 1
        dp = [0] * (n + 1)
        dp[1], dp[2] = 1, 2
        for i in range(3, len(dp)):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[-1]
