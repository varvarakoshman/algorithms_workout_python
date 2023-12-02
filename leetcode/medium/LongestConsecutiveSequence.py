import unittest
from typing import (
    List,
)


# O(n) time | O(n) space
class Solution(object):
    def longestConsecutive(self, nums: List[int]) -> int:
        unique_nums = set()
        for num in nums:
            unique_nums.add(num)

        max_len = 0
        for num in nums:
            if num + 1 in unique_nums:
                continue
            curr_len = 0
            while num in unique_nums:
                curr_len += 1
                num -= 1
            max_len = max(max_len, curr_len)

        return max_len


class MyTestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual(9, Solution().longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
        self.assertEqual(4, Solution().longestConsecutive([100, 4, 200, 1, 3, 2]))
