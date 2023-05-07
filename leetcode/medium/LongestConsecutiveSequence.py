import unittest


# O(n) time | O(n) space
class Solution(object):
    def longestConsecutive(self, nums):
        longest_len = 0
        values_set, already_seen = set(), set()
        for num in nums:
            values_set.add(num)
        for num in nums:
            if num - 1 not in values_set and num not in already_seen:
                curr_len = 1
                while num + curr_len in values_set:
                    curr_len += 1
                already_seen.add(num)
                longest_len = max(longest_len, curr_len)
        return longest_len


class MyTestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual(9, Solution().longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
        self.assertEqual(4, Solution().longestConsecutive([100, 4, 200, 1, 3, 2]))
