# O(n) time | O(n) space
class Solution1:
    def minCostClimbingStairs(self, cost):
        dp = [0] * len(cost)
        for i in range(2, len(cost)):
            two_step_cost = dp[i - 2] + cost[i - 2]
            one_step_cost = dp[i - 1] + cost[i - 1]
            dp[i] = min(one_step_cost, two_step_cost)
        last_idx = len(cost) - 1
        return min(dp[last_idx - 1] + cost[last_idx - 1], dp[last_idx] + cost[last_idx])


# O(n) time | O(1) space
class Solution2:
    def minCostClimbingStairs(self, cost):
        prev_prev, prev = 0, 0
        for i in range(2, len(cost) + 1):
            new_prev = min(prev + cost[i - 1], prev_prev + cost[i - 2])
            prev_prev = prev
            prev = new_prev
        return prev


if __name__ == '__main__':
    solutions = [Solution1(), Solution2()]
    for solution in solutions:
        assert solution.minCostClimbingStairs([10, 15, 20]) == 15
        assert solution.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) == 6

