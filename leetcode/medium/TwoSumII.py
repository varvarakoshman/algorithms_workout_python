# O(n) time | O(1) space
def twoSum(numbers, target):
    left = 0
    right = len(numbers) - 1
    while left < right:
        curr_sum = numbers[left] + numbers[right]
        if curr_sum > target:
            right -= 1
        elif curr_sum < target:
            left += 1
        else:
            return [left + 1, right + 1]
    return [-1, -1]


if __name__ == '__main__':
    assert twoSum([2, 7, 11, 15], 9) == [1, 2]
    assert twoSum([2, 7, 11, 15], 17) == [1, 4]
    assert twoSum([2, 7, 11, 15], 18) == [2, 3]
    assert twoSum([2, 7, 11, 15], 22) == [2, 4]
    assert twoSum([2, 3, 4], 6) == [1, 3]
    assert twoSum([2, 3], 5) == [1, 2]
    assert twoSum([-1, 0], -1) == [1, 2]
