from typing import (
    List,
)


# O(n) time | O(1) space
class Solution1:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        moved_count = 0
        start_idx = 0

        while moved_count < n:
            curr_idx = start_idx
            prev = nums[start_idx]
            while True:
                next_idx = (curr_idx + k) % n
                nums[next_idx], prev = prev, nums[next_idx]
                curr_idx = next_idx
                moved_count += 1

                if start_idx == curr_idx:
                    break
            start_idx += 1


# O(n) time | O(1) space
class Solution2:
    def rotate(self, nums: List[int], k: int) -> None:
        k %= len(nums)
        nums.reverse()
        self.reverse_subarray(nums, 0, k - 1)
        self.reverse_subarray(nums, k, len(nums) - 1)

    def reverse_subarray(self, nums,  start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1


if __name__ == '__main__':
    solutions = [Solution1(), Solution2()]

    for solution in solutions:
        test = [1, 2, 3, 4, 5, 6, 7]
        solution.rotate(test, 3)
        assert test == [5, 6, 7, 1, 2, 3, 4]

        test = [-1, -100, 3, 99]
        solution.rotate(test, 2)
        assert test == [3, 99, -1, -100]

        test = [1]
        solution.rotate(test, 0)
        assert test == [1]

        test = [-1]
        solution.rotate(test, 2)
        assert test == [-1]
