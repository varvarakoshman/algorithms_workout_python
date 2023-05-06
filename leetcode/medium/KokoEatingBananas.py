import math


# O(n*log(max(piles)) time, n=len(piles) | O(1) space
class Solution(object):
    def minEatingSpeed(self, piles, h):
        left, right = 1, max(piles)
        optimal_k = right
        while left <= right:
            k = (left + right) // 2
            curr_h = self.get_hours_by_k(piles, k)
            if curr_h <= h:
                optimal_k = min(optimal_k, k)
                right = k - 1
            else:
                left = k + 1
        return optimal_k

    def get_hours_by_k(self, piles, k):
        total_hours = 0
        for pile in piles:
            total_hours += math.ceil(pile / k)
        return total_hours


if __name__ == '__main__':
    assert Solution().minEatingSpeed([3, 6, 7, 11], 8) == 4
    assert Solution().minEatingSpeed([30, 11, 23, 4, 20], 5) == 30
    assert Solution().minEatingSpeed([30, 11, 23, 4, 20], 6) == 23
