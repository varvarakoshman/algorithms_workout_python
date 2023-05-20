import unittest


# O(n*2^n) time | O(n*2^n) space
class Solution:
    def subsetsWithDup_(self, nums):
        nums.sort()
        subsets = set()
        subsets.add(tuple([]))
        for num in nums:
            for subset in list(subsets):
                new_subset = tuple(list(subset) + [num])
                subsets.add(new_subset)
        return list(subsets)

    # O(n*2^n) time | O(n*2^n) space
    def subsetsWithDup(self, nums):
        nums.sort()
        result = []

        def backtrack(idx, subset):
            if idx == len(nums):
                result.append(subset[:])
                return

            subset.append(nums[idx])
            backtrack(idx + 1, subset)
            subset.pop()

            while idx + 1 < len(nums) and nums[idx] == nums[idx + 1]:
                idx += 1
            backtrack(idx + 1, subset)

        backtrack(0, [])
        return result



class TestProgram(unittest.TestCase):
    def test_case_1(self):
        expected = [[[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]]
        actual = Solution().subsetsWithDup([1, 2, 2])
        self.assertEqual(expected, actual)

    def test_case_2(self):
        expected = [[[], [1], [1, 1], [1, 2], [1, 1, 2], [1, 2, 2], [2], [2, 2], [1, 1, 2, 2]]]
        actual = Solution().subsetsWithDup([1, 2, 2, 1])
        self.assertEqual(expected, actual)

    def test_case_3(self):
        expected = [[], [0]]
        actual = Solution().subsetsWithDup([0])
        self.assertEqual(expected, actual)
