import unittest


# O(logn) time | O(1) space
class Solution(object):
    def search(self, nums, target):
        left, right = 0, len(nums) - 1
        while left < right:
            if right - left <= 1:
                break
            middle = (left + right) // 2
            left_growth = nums[middle] - nums[left]
            right_growth = nums[right] - nums[middle]
            is_contained_left = nums[left] <= target <= nums[middle]
            is_contained_right = nums[middle] <= target <= nums[right]
            if left_growth >= 0 and right_growth >= 0:
                if is_contained_left:
                    return self.binary_search(nums, left, middle, target)
                elif is_contained_right:
                    return self.binary_search(nums, middle, right, target)
                return -1
            elif right_growth >= 0:
                if is_contained_right:
                    return self.binary_search(nums, middle, right, target)
                right = middle
            elif left_growth >= 0:
                if is_contained_left:
                    return self.binary_search(nums, left, middle, target)
                left = middle
        if nums[left] == target:
            return left
        elif nums[right] == target:
            return right
        return -1

    def binary_search(self, nums, start, end, target):
        while start <= end:
            middle = (start + end) // 2
            if nums[middle] > target:
                end = middle - 1
            elif nums[middle] < target:
                start = middle + 1
            else:
                return middle
        return -1


class MyTestCase(unittest.TestCase):
    def test_1(self):
        input = [4, 5, 6, 7, 0, 1, 2]
        self.assertEqual(4, Solution().search(input, 0))

    def test_2(self):
        input = [4, 5, 6, 7, 0, 1, 2]
        self.assertEqual(-1, Solution().search(input, 3))

    def test_3(self):
        input = [1]
        self.assertEqual(-1, Solution().search(input, 0))

    def test_4(self):
        input = [1]
        self.assertEqual(0, Solution().search(input, 1))

    def test_5(self):
        input = [3, 1]
        self.assertEqual(1, Solution().search(input, 1))
