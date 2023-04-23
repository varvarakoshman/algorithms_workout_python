# 1-dp
# O(n^2) time | O(n) space
def lengthOfLIS(nums):
    max_len = 1
    dp = [1] * len(nums)
    for i in range(len(nums)):
        for j in range(i):
            if nums[j] < nums[i] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                max_len = max(max_len, dp[j] + 1)
    return max_len


if __name__ == '__main__':
    assert lengthOfLIS([4, 10, 5, 12, 3, 24, 7, 8]) == 4
    assert lengthOfLIS([5, 4, 3, 2, 1]) == 1
    assert lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]) == 4
    assert lengthOfLIS([0, 1, 0, 3, 2, 3]) == 4
    assert lengthOfLIS([7, 7, 7, 7, 7, 7]) == 1
    assert lengthOfLIS([1, 3, 6, 7, 9, 4, 10, 5, 6]) == 6
