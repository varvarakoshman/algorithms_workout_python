# O(n) time | O(n) space
class Solution(object):
    def dailyTemperatures(self, temperatures):
        warmer_days = [0] * len(temperatures)
        stack = [tuple([0, temperatures[0]])]
        for i in range(1, len(temperatures)):
            curr_temp = temperatures[i]
            while len(stack) > 0 and stack[-1][1] < curr_temp:
                prev_idx = stack.pop()[0]
                warmer_days[prev_idx] = i - prev_idx
            stack.append(tuple([i, curr_temp]))
        return warmer_days


if __name__ == '__main__':
    assert Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [1, 1, 4, 2, 1, 1, 0, 0]
    assert Solution().dailyTemperatures([30, 40, 50, 60]) == [1, 1, 1, 0]
    assert Solution().dailyTemperatures([30, 60, 90]) == [1, 1, 0]
