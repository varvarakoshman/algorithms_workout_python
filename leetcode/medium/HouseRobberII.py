# O(n) time | O(n) space
class Solution1:
    def rob(self, nums):
        if len(nums) == 0:
            return 0

        dp1 = [-1] * (len(nums) + 1)
        dp1[1] = nums[0]
        dp2 = [-1] * (len(nums) + 1)
        dp2[1] = 0
        dp1[0], dp2[0] = 0, 0

        for i in range(1, len(nums) - 1):
            dp1[i + 1] = max(dp1[i - 1] + nums[i], dp1[i])
            dp2[i + 1] = max(dp2[i - 1] + nums[i], dp2[i])
        dp1[len(nums)] = dp1[len(nums) - 1]
        dp2[len(nums)] = max(dp2[len(nums) - 2] + nums[len(nums) - 1], dp2[len(nums) - 1])
        return max(dp1[-1], dp2[-1])


# O(n) time | O(1) space
class Solution2:
    def rob(self, nums):
        if len(nums) == 0:
            return 0

        dp1_prev_prev = 0
        dp1_prev = nums[0]
        dp2_prev_prev = 0
        dp2_prev = 0

        for i in range(1, len(nums) - 1):
            dp1_prev_new = max(dp1_prev_prev + nums[i], dp1_prev)
            dp1_prev_prev = dp1_prev
            dp1_prev = dp1_prev_new

            dp2_prev_new = max(dp2_prev_prev + nums[i], dp2_prev)
            dp2_prev_prev = dp2_prev
            dp2_prev = dp2_prev_new

        dp2_prev = max(dp2_prev_prev + nums[len(nums) - 1], dp2_prev)
        return max(dp1_prev, dp2_prev)


if __name__ == '__main__':
    solutions = [Solution1(), Solution2()]
    for solution in solutions:
        assert solution.rob([2, 3, 2]) == 3
        assert solution.rob([1, 2, 3, 1]) == 4
        assert solution.rob([1, 2, 3]) == 3
        assert solution.rob([5, 2, 4, 1, 2, 8]) == 12
        assert solution.rob([5, 2, 4, 1, 20, 8]) == 29
        assert solution.rob([]) == 0
