# O(n^2) time | O(n) space
def threeSum(nums):
    triplets = set()
    nums.sort()
    for i in range(len(nums) - 1):
        left, right = i + 1, len(nums) - 1
        curr_num = nums[i]
        while left < right:
            curr_sum = curr_num + nums[left] + nums[right]
            if curr_sum > 0:
                right -= 1
            elif curr_sum < 0:
                left += 1
            else:
                triplets.add(tuple([curr_num, nums[left], nums[right]]))
                left += 1
                right -= 1
    return list(triplets)


if __name__ == '__main__':
    assert threeSum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
    assert threeSum([0, 1, 1]) == []
    assert threeSum([0, 0, 0]) == [[0, 0, 0]]
    assert threeSum([0, -1, 1, 1, 0, -1]) == [[-1, 0, 1]]
