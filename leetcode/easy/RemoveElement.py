import unittest


# O(n) time | O(1) space
def removeElement(nums, val):
    left_pointer, right_pointer = 0, 0
    while left_pointer < len(nums) and right_pointer < len(nums):
        if nums[left_pointer] == val:
            right_pointer = left_pointer + 1
            while right_pointer < len(nums):
                if nums[right_pointer] == val:
                    right_pointer += 1
                else:
                    nums[left_pointer], nums[right_pointer] = nums[right_pointer], nums[left_pointer]
                    break
        left_pointer += 1
    right_pointer = len(nums) - 1
    while right_pointer >= 0 and nums[right_pointer] == val:
        del nums[right_pointer]
        right_pointer -= 1

# a better approach ....
# // O(n) time | O(1) space
# class Solution {
#     public int removeElement(int[] nums, int val) {
#         int i = 0;
#         int k = nums.length;
#         while (i < k) {
#             if (nums[i] == val) {
#                 nums[i] = nums[k - 1];
#                 k--;
#             } else {
#                 i++;
#             }
#         }
#         return k;
#     }
# }


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = [0, 1, 2, 2, 3, 0, 4, 2]
        expected = [0, 1, 3, 0, 4, 2, 2, 2]
        removeElement(input, 2)
        self.assertEqual(input, expected)
