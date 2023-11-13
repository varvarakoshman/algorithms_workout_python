from typing import (
    List,
)


# O(n) time | O(1) space
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        pointer1 = m - 1
        pointer2 = n - 1
        curr_index = len(nums1) - 1
        while pointer2 >= 0 and pointer1 >= 0:
            if nums1[pointer1] >= nums2[pointer2]:
                nums1[curr_index] = nums1[pointer1]
                pointer1 -= 1
            else:
                nums1[curr_index] = nums2[pointer2]
                pointer2 -= 1
            curr_index -= 1
        if pointer2 >= 0:
            while pointer2 >= 0:
                nums1[curr_index] = nums2[pointer2]
                curr_index -= 1
                pointer2 -= 1
        return nums1


if __name__ == '__main__':
    solution = Solution()
    assert solution.merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3) == [1, 2, 2, 3, 5, 6]
    assert solution.merge([0], 0, [1], 1) == [1]
    assert solution.merge([5, 6, 7, 0, 0, 0], 3, [1, 2, 3], 3) == [1, 2, 3, 5, 6, 7]
    assert solution.merge([4, 0, 0, 0, 0, 0], 1, [1, 2, 3, 5, 6], 5) == [1, 2, 3, 4, 5, 6]
    assert solution.merge([1, 2, 3, 4, 0], 4, [5], 1) == [1, 2, 3, 4, 5]
