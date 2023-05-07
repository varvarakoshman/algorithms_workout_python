import unittest


# Solution 1 (negative marking)
# O(n) time | O(1) space
class Solution1:
    def findDuplicate(self, nums):
        duplicate = None
        for num in nums:
            curr_num = abs(num)
            if nums[curr_num] < 0:
                duplicate = curr_num
                break
            nums[curr_num] = -1 * nums[curr_num]
        for i in range(len(nums)):
            nums[i] = abs(nums[i])
        return duplicate


# Solution 2 (Array as HashMap (Iterative))
# O(n) time | O(1) space
class Solution2:
    def findDuplicate(self, nums):
        while nums[0] != nums[nums[0]]:
            nums[nums[0]], nums[0] = nums[0], nums[nums[0]]
        return nums[0]


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        # # nums = [1,3,4,2,2]
        # # => 2
        # self.assertEqual(2, Solution1().findDuplicate([1, 3, 4, 2, 2]))
        # self.assertEqual(2, Solution2().findDuplicate([1, 3, 4, 2, 2]))
        # # nums = [3,1,3,4,2]
        # # => 3
        # self.assertEqual(3, Solution1().findDuplicate([3, 1, 3, 4, 2]))
        # self.assertEqual(3, Solution2().findDuplicate([3, 1, 3, 4, 2]))

        self.assertEqual(3, Solution1().findDuplicate([3, 3, 5, 4, 1, 3]))
        self.assertEqual(3, Solution2().findDuplicate([3, 3, 5, 4, 1, 3]))
