import unittest


# O(n*logn) time | O(n) space
class Solution(object):
    def carFleet(self, target, position, speed):
        position_speed_ordered = [[position[i], speed[i]] for i in range(len(position))]
        position_speed_ordered.sort(key=lambda x: x[0])
        stack = []
        for i in range(len(position_speed_ordered)):
            distance = target - position_speed_ordered[i][0]
            time = distance / position_speed_ordered[i][1]
            stack.append(time)
        fleet_count = 1
        top_car_time = stack.pop()
        while len(stack) > 0:
            curr_car_time = stack.pop()
            if curr_car_time > top_car_time:
                fleet_count += 1
                top_car_time = curr_car_time
        return fleet_count


class MyTestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual(1, Solution().carFleet(10, [0, 4, 2], [2, 1, 3]))
        self.assertEqual(2, Solution().carFleet(10, [6, 8], [3, 2]))
        self.assertEqual(3, Solution().carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]))
        self.assertEqual(1, Solution().carFleet(10, [3], [3]))
        self.assertEqual(1, Solution().carFleet(100, [0, 2, 4], [4, 2, 1]))
