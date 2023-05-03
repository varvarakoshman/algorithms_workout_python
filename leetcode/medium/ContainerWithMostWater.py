# O(n) time | O(1) space
class Solution(object):
    def maxArea(self, height):
        right = len(height) - 1
        left, max_area = 0, 0
        while left < right:
            curr_area = (right - left) * min(height[left], height[right])
            max_area = max(max_area, curr_area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area


if __name__ == '__main__':
    assert Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert Solution().maxArea([1, 1]) == 1
    assert Solution().maxArea([2, 3, 10, 5, 7, 8, 9]) == 36
