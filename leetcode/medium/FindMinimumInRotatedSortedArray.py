# O(logn) time | O(1) space
class Solution(object):
    def findMin(self, nums):
        left, right = 0, len(nums) - 1
        while left < right:
            if right - left == 1:
                break
            middle = (left + right) // 2
            left_growth = nums[middle] - nums[left]
            right_growth = nums[right] - nums[middle]
            if left_growth < 0:
                right = middle
            elif right_growth < 0:
                left = middle
            else:
                return nums[0]
        return min(nums[left], nums[right])


if __name__ == '__main__':
    assert Solution().findMin([4, 5, 6, 7, 0, 1, 2]) == 0
    assert Solution().findMin([11, 13, 15, 17]) == 11
