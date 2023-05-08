# Solution 1 - wrapping a 3Sum with an extra for loop
# O(n^3) time | O(1) space
class Solution1(object):
    def fourSum(self, nums, target):
        result = set()
        nums.sort()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                left = j + 1
                right = len(nums) - 1
                while left < right:
                    curr_sum = nums[i] + nums[j] + nums[left] + nums[right]
                    if curr_sum > target:
                        right -= 1
                    elif curr_sum < target:
                        left += 1
                    else:
                        result.add(tuple([nums[i], nums[j], nums[left], nums[right]]))
                        left += 1
                        right -= 1
        return result


# Solution 2 - generalisation for k Sum
# O(n^3) time | O(n) space
class Solution2(object):

    def fourSum(self, nums, target):
        result, curr_quad = [], []

        def k_sum_getter(k, start, target):
            if k != 2:
                for i in range(start, len(nums) - k + 1):
                    if i > start and nums[i] == nums[i - 1]:
                        continue
                    curr_quad.append(nums[i])
                    k_sum_getter(k - 1, i + 1, target - nums[i])
                    curr_quad.pop()
            else:
                left, right = start, len(nums) - 1
                while left < right:
                    curr_sum = nums[left] + nums[right]
                    if curr_sum > target:
                        right -= 1
                    elif curr_sum < target:
                        left += 1
                    else:
                        result.append(curr_quad + [nums[left], nums[right]])
                        left += 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1

        nums.sort()
        k_sum_getter(4, 0, target)
        return result


if __name__ == '__main__':
    assert Solution1().fourSum([1, 0, -1, 0, -2, 2], 0) == [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
    assert Solution1().fourSum([2, 2, 2, 2, 2], 8) == [[2, 2, 2, 2]]

    assert Solution2().fourSum([1, 0, -1, 0, -2, 2], 0) == [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
    assert Solution2().fourSum([2, 2, 2, 2, 2], 8) == [[2, 2, 2, 2]]
