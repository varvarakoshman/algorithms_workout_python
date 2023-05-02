# O(n) time | O(1) space
class Solution(object):
    def maxProfit(self, prices):
        max_profit = 0
        left, right = 0, 0
        while right < len(prices):
            if prices[right] < prices[left]:
                left = right
            max_profit = max(max_profit, prices[right] - prices[left])
        return max_profit


if __name__ == '__main__':
    assert Solution().maxProfit([7, 1, 5, 3, 6, 4]) == 5
    assert Solution().maxProfit([7, 6, 4, 3, 1]) == 0
    assert Solution().maxProfit([1, 2, 3, 4, 5]) == 4
    assert Solution().maxProfit([1]) == 0
    assert Solution().maxProfit([2, 1, 4]) == 3
    assert Solution().maxProfit([2, 1, 2, 1, 0, 1, 2]) == 2
