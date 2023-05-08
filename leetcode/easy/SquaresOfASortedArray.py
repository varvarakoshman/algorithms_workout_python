import unittest

# O(n) time | O(n) space
class Solution:
    def sortedSquares(self, nums):
        output = [0] * len(nums)
        output_idx = len(output) - 1
        left, right = 0, len(nums) - 1
        while left <= right:
            if abs(nums[right]) >= abs(nums[left]):
                output[output_idx] = nums[right] * nums[right]
                right -= 1
            else:
                output[output_idx] = nums[left] * nums[left]
                left += 1
            output_idx -= 1
        return output


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual([0, 1, 9, 16, 100], Solution().sortedSquares([-4, -1, 0, 3, 10]))
        self.assertEqual([4, 9, 9, 49, 121], Solution().sortedSquares([-7, -3, 2, 3, 11]))
        self.assertEqual([1, 4, 9, 16], Solution().sortedSquares([1, 2, 3, 4]))
        self.assertEqual([1, 4, 9, 16], Solution().sortedSquares([-4, -3, -2, -1]))
        self.assertEqual([0, 0, 0], Solution().sortedSquares([0, 0, 0]))
        self.assertEqual([1], Solution().sortedSquares([1]))
        self.assertEqual([16], Solution().sortedSquares([-4]))
        self.assertEqual([], Solution().sortedSquares([]))
