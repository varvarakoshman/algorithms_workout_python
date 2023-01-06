# O(n) time | O(n) space
def zeroSumSubarray(nums):
    sums = set()
    curr_sum = 0
    for num in nums:
        curr_sum += num
        if curr_sum in sums or curr_sum == 0:
            return True
        sums.add(curr_sum)
    return False


if __name__ == '__main__':
    assert zeroSumSubarray([-5, -5, 2, 3, -2]) is True
    assert zeroSumSubarray([10, 5, 2, 2, -10]) is False
    assert zeroSumSubarray([1, 2, 3, -3, -2, -1]) is True
    assert zeroSumSubarray([1, 2, 3, 4, 0, 5, 6]) is True
    assert zeroSumSubarray([1, 2, 3, 4, 5, 6]) is False
    assert zeroSumSubarray([-1, -2, -3, -4, -5, -6]) is False
    assert zeroSumSubarray([]) is False
