from typing import (
    List,
)


# O(n^2) time | O(n) space
def threeSum(nums: List[int]) -> List[List[int]]:
    result = []
    nums.sort()
    for i in range(len(nums)):
        if nums[i] > 0:
            break
        if i == 0 or nums[i] != nums[i - 1]:
            twoSum(nums, i, result)
    return result


def twoSum(nums, curr_idx, result):
    first = nums[curr_idx]
    left = curr_idx + 1
    right = len(nums) - 1
    target_sum = -first

    while left < right:
        curr_sum = nums[left] + nums[right]
        if curr_sum < target_sum:
            left += 1
        elif curr_sum > target_sum:
            right -= 1
        else:
            result.append([first, nums[left], nums[right]])
            left += 1
            right -= 1

            while left < right and nums[left] == nums[left - 1]:
                left += 1


if __name__ == '__main__':
    assert threeSum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
    assert threeSum([0, 1, 1]) == []
    assert threeSum([0, 0, 0]) == [[0, 0, 0]]
    assert threeSum([0, -1, 1, 1, 0, -1]) == [[-1, 0, 1]]
