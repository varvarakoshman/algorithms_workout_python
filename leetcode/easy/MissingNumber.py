# Possible worse solutions:
# 1) O(n*logn) time | O(1) space (with sorting)
# 2) O(n) time | O(n) space (with a hashset)

# O(n) time | O(1) space
# Ex: [3, 0, 1]
# [0, 1, 2, 3] XOR [3, 0, 1] = (0 ^ 1 ^ 2 ^ 3) ^ (3 ^ 0 ^ 1) = 2
class Solution:
    def missingNumber(self, nums):
        result = len(nums)
        for i in range(len(nums)):
            result ^= i ^ nums[i]
        return result


if __name__ == '__main__':
    solution = Solution()
    assert solution.missingNumber([3, 0, 1]) == 2
    assert solution.missingNumber([3, 2, 1]) == 0
    assert solution.missingNumber([0, 1]) == 2
    assert solution.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]) == 8
    assert solution.missingNumber([2, 0]) == 1
