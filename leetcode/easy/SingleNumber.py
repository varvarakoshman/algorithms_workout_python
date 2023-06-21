# O(n) time | O(1) space
class Solution:
    def singleNumber(self, nums):
        single_number = nums[0]
        for i in range(1, len(nums)):
            single_number = single_number ^ nums[i]
        return single_number


if __name__ == '__main__':
    solution = Solution()
    assert solution.singleNumber([2, 2, 1]) == 1
    assert solution.singleNumber([4, 1, 2, 1, 2]) == 4
    assert solution.singleNumber([1, 1, 2, 2, 5]) == 5
    assert solution.singleNumber([1, 1, 5, 2, 2]) == 5
    assert solution.singleNumber([1, 1, 2, 2, 0]) == 0
    assert solution.singleNumber([1]) == 1
