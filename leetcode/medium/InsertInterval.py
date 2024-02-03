from typing import List


# O(n) time | O(n) space
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        merged_result = []
        for interval in intervals:
            if interval[1] < newInterval[0]:
                merged_result.append(interval)
            elif interval[0] > newInterval[1]:
                merged_result.append(newInterval)
                newInterval = interval
            else:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])
        merged_result.append(newInterval)
        return merged_result
