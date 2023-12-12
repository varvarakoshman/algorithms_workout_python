from typing import (
    List,
)


# O(n) time | O(n) space
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ranges = []
        left = 0
        while left < len(nums):
            right = left
            while right + 1 < len(nums) and nums[right + 1] - 1 == nums[right]:
                right += 1
            if right == left:
                ranges.append(str(nums[left]))
            else:
                ranges.append(str(nums[left]) + "->" + str(nums[right]))
            left = right + 1
        return ranges


if __name__ == '__main__':
    solution = Solution()
    assert solution.summaryRanges([0, 1, 2, 4, 5, 7]) == ["0->2", "4->5", "7"]
    assert solution.summaryRanges([0, 2, 3, 4, 6, 8, 9]) == ["0", "2->4", "6", "8->9"]
