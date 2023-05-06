import unittest


class TimeMap(object):

    def __init__(self):
        self.time_map = {}

    # O(1) time | O(1) space
    def set(self, key, value, timestamp):
        if key not in self.time_map:
            self.time_map[key] = []
        self.time_map[key].append(tuple([value, timestamp]))

    # O(logn) time | O(1) space
    def get(self, key, timestamp):
        if key not in self.time_map:
            return ""
        return self.get_closest_value(self.time_map[key], timestamp)

    def get_closest_value(self, timestamp_tuples, target):
        left, right = 0, len(timestamp_tuples) - 1
        result = ""
        while left <= right:
            middle = (left + right) // 2
            if timestamp_tuples[middle][1] <= target:
                left = middle + 1
                result = timestamp_tuples[middle][0]
            else:
                right = middle - 1
        return result


class MyTestCase(unittest.TestCase):
    def test_1(self):
        timeMap = TimeMap()

        timeMap.set("foo", "bar", 1)
        self.assertEqual("bar", timeMap.get("foo", 1))
        self.assertEqual("bar", timeMap.get("foo", 3))

        timeMap.set("foo", "bar2", 4)
        self.assertEqual("bar2", timeMap.get("foo", 4))
        self.assertEqual("bar2", timeMap.get("foo", 5))
