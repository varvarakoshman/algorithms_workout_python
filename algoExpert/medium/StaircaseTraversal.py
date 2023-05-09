import unittest


# O(n*maxSteps) time | O(n) space
# recursive dp
class Solution1:
    def staircaseTraversal(self, height, maxSteps):
        dp = {0: 1, 1: 1}
        self.traversal(dp, height, maxSteps)
        return dp[height]

    def traversal(self, dp, curr_height, maxSteps):
        if curr_height in dp:
            return dp[curr_height]

        possible_steps = 0
        for step in range(1, min(maxSteps, curr_height) + 1):
            possible_steps += self.traversal(dp, curr_height - step, maxSteps)

        dp[curr_height] = possible_steps
        return possible_steps


# O(n*maxSteps) time | O(n) space
# iterative dp
class Solution2:
    def staircaseTraversal(self, height, maxSteps):
        dp = [0] * (height + 1)
        dp[0], dp[1] = 1, 1
        for i in range(2, height + 1):
            step_num = min(maxSteps, height)
            for step in range(1, step_num + 1):
                dp[i] += dp[i - step]
        return dp[-1]


# O(n) time | O(n) space
# sliding window
# (Optimal solution)
class Solution3:
    def staircaseTraversal(self, height, maxSteps):
        current_number_of_ways = 0
        ways_to_top = [1]

        for current_height in range(1, height + 1):
            start_of_window = current_height - maxSteps - 1 # start of a previous window
            end_of_window = current_height - 1

            if start_of_window >= 0:
                current_number_of_ways -= ways_to_top[start_of_window]

            current_number_of_ways += ways_to_top[end_of_window]
            ways_to_top.append(current_number_of_ways)

        return ways_to_top[height]


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        solutions = [Solution1(), Solution2(), Solution3()]
        stairs = 4
        maxSteps = 2
        expected = 5
        for solution in solutions:
            actual = solution.staircaseTraversal(stairs, maxSteps)
            self.assertEqual(actual, expected)
