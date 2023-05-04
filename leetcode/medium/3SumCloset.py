# O(n) time | O(1) space
class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        closest_diff, closest_sum = float('inf'), 0
        for i, num in enumerate(nums):
            left, right = i + 1, len(nums) - 1
            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]
                curr_diff = abs(curr_sum - target)
                if curr_diff < closest_diff:
                    closest_diff = curr_diff
                    closest_sum = curr_sum
                if curr_sum > target:
                    right -= 1
                else:
                    left += 1
        return closest_sum


if __name__ == '__main__':
    assert Solution().threeSumClosest([-1, 2, 1, -4], 1) == 2
    assert Solution().threeSumClosest([0, 0, 0], 1) == 0
