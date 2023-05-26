# O(n) time | O(n) space
class Solution1:
    def rob(self, nums):
        if len(nums) == 0:
            return 0
        dp = [-1] * (len(nums) + 1)
        dp[0], dp[1] = 0, nums[0]
        for i in range(1, len(nums)):
            dp[i + 1] = max(dp[i - 1] + nums[i], dp[i])
        return dp[-1]


# O(n) time | O(1) space
class Solution2:
    def rob(self, nums):
        if len(nums) == 0:
            return 0
        prev_prev, prev = 0, nums[0]
        for i in range(1, len(nums)):
            new_prev = max(prev_prev + nums[i], prev)
            prev_prev = prev
            prev = new_prev
        return prev


if __name__ == '__main__':
    solutions = [Solution1(), Solution2()]
    for solution in solutions:
        assert solution.rob([1, 2, 3, 1]) == 4
        assert solution.rob([2, 7, 9, 3, 1]) == 12
        assert solution.rob([]) == 0
        assert solution.rob([1, 1, 1, 1, 1]) == 3
        assert solution.rob([1, 5]) == 5
        assert solution.rob([5, 0]) == 5
        assert solution.rob([5, 2, 4, 1, 2, 8]) == 17
