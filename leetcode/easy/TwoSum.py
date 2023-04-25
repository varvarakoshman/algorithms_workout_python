# O(n) time | O(n) space
def twoSum(nums, target):
    remainders = {}
    for idx, num in enumerate(nums):
        if num in remainders:
            return [remainders[num], idx]
        remainders[target - num] = idx
    return []


if __name__ == '__main__':
    assert twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert twoSum([3, 2, 4], 6) == [1, 2]
    assert twoSum([3, 3], 6) == [0, 1]
