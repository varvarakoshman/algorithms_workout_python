from typing import List


# O(n*logn) time | O(1) space
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[0])
        prev_end = points[0][1]
        count = 1
        for i in range(1, len(points)):
            current = points[i]
            if prev_end < current[0]:
                count += 1
                prev_end = current[1]
            else:
                prev_end = min(prev_end, current[1])
        return count
