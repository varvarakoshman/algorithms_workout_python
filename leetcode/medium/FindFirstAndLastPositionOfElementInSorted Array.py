# [5, 7, 7, 8, 8, 10, 11, 12, 13, 14, 15, 16]
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
from typing import List


# O(nlogn) time | O(1) space
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first_idx = self.find_first_occurence(nums, target)
        last_idx = self.find_last_occurence(nums, target)
        return [first_idx, last_idx]

    def find_first_occurence(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            middle = left + (right - left) // 2
            if target < nums[middle]:
                right = middle - 1
            elif target > nums[middle]:
                left = middle + 1
            else:
                if middle - 1 < 0 or middle - 1 >= 0 and nums[middle - 1] != target:
                    return middle
                else:
                    right = middle - 1
        return -1

    def find_last_occurence(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            middle = left + (right - left) // 2
            if target < nums[middle]:
                right = middle - 1
            elif target > nums[middle]:
                left = middle + 1
            else:
                if middle + 1 >= len(nums) or middle + 1 < len(nums) and nums[middle + 1] != target:
                    return middle
                else:
                    left = middle + 1
        return -1
