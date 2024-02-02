from typing import List


# 1)
# ____ ____

# 2)
# 1: _____
# 2:  __

# 3)
# 1: _____
# 2:    _____

# O(n*log(n)) time | O(n) space
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        merged = [intervals[0]]
        for i in range(1, len(intervals)):
            curr_interval = intervals[i]
            if merged[-1][1] < curr_interval[0]:
                merged.append(curr_interval)  # 1)
            else:
                merged[-1][1] = max(merged[-1][1], curr_interval[1])  # 2) + 3)
        return merged


if __name__ == '__main__':
    solution = Solution()
    assert solution.merge([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
    assert solution.merge([[1, 3], [4, 9], [8, 10]]) == [[1, 3], [4, 10]]
    assert solution.merge([[1, 3], [4, 18], [8, 10]]) == [[1, 3], [4, 18]]
    assert solution.merge([[4, 18], [8, 10], [9, 20]]) == [[4, 20]]
