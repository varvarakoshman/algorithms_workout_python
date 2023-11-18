from typing import (
    List,
)


# O(n) time | O(1) space
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        insert_idx = 1
        for curr_idx in range(1, len(nums)):
            if nums[curr_idx] != nums[curr_idx - 1]:
                nums[insert_idx] = nums[curr_idx]
                insert_idx += 1
        return insert_idx


if __name__ == '__main__':
    solution = Solution()
    assert solution.removeDuplicates([1, 1, 2]) == 2
    assert solution.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]) == 5
