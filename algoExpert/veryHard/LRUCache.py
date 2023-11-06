import unittest


class LRUCache:

    def __init__(self, max_size):
        self.maxSize = max_size or 1
        self.cache = {}
        self.most_recent = None
        self.curr_capacity = 0
        self.least_recent = None

    # O(1) time | O(1) space
    def insertKeyValuePair(self, key, value):
        if key in self.cache:
            self.cache[key].value = value
            return

        if self.curr_capacity == self.maxSize:
            del self.cache[self.least_recent.key]
            self.least_recent = self.least_recent.next
            if self.least_recent and self.least_recent.next:
                self.least_recent.next.prev = None
            self.curr_capacity -= 1

        new_node = self.Node(key, value)
        new_node.prev = self.most_recent
        if self.most_recent:
            self.most_recent.next = new_node
        self.most_recent = new_node
        self.curr_capacity += 1
        self.cache[key] = new_node

        if self.curr_capacity == 1:
            self.least_recent = new_node

    # O(1) time | O(1) space
    def getValueFromKey(self, key):
        if key not in self.cache:
            return None

        target = self.cache[key]
        if self.least_recent == target and self.least_recent.next:
            self.least_recent = self.least_recent.next
        before_target = target.prev
        after_target = target.next
        if before_target:
            before_target.next = after_target
        if after_target:
            after_target.prev = before_target

        target.next = None
        target.prev = self.most_recent
        if self.most_recent:
            self.most_recent.next = target
        self.most_recent = target
        return target.value

    # O(1) time | O(1) space
    def getMostRecentKey(self):
        return self.most_recent.key if self.most_recent else None

    class Node:
        def __init__(self, key, value, prev=None, next=None):
            self.key = key
            self.value = value
            self.prev = prev
            self.next = next


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        lruCache = LRUCache(3)
        lruCache.insertKeyValuePair("b", 2)
        lruCache.insertKeyValuePair("a", 1)
        lruCache.insertKeyValuePair("c", 3)
        self.assertEqual(lruCache.getMostRecentKey(), "c")
        self.assertEqual(lruCache.getValueFromKey("a"), 1)
        self.assertEqual(lruCache.getMostRecentKey(), "a")
        lruCache.insertKeyValuePair("d", 4)
        self.assertEqual(lruCache.getValueFromKey("b"), None)
        lruCache.insertKeyValuePair("a", 5)
        self.assertEqual(lruCache.getValueFromKey("a"), 5)

    def test_case_2(self):
        lruCache = LRUCache(1)
        self.assertEqual(lruCache.getValueFromKey("a"), None)
        lruCache.insertKeyValuePair("a", 1)
        self.assertEqual(lruCache.getValueFromKey("a"), 1)
        lruCache.insertKeyValuePair("a", 9001)
        self.assertEqual(lruCache.getValueFromKey("a"), 9001)
        lruCache.insertKeyValuePair("b", 2)
        self.assertEqual(lruCache.getValueFromKey("a"), None)
        self.assertEqual(lruCache.getValueFromKey("b"), 2)
        lruCache.insertKeyValuePair("c", 3)
        self.assertEqual(lruCache.getValueFromKey("a"), None)
        self.assertEqual(lruCache.getValueFromKey("b"), None)
        self.assertEqual(lruCache.getValueFromKey("c"), 3)

    def test_case_3(self):
        lruCache = LRUCache(4)
        lruCache.insertKeyValuePair("a", 1)
        lruCache.insertKeyValuePair("b", 2)
        lruCache.insertKeyValuePair("c", 3)
        lruCache.insertKeyValuePair("d", 4)
        self.assertEqual(lruCache.getValueFromKey("a"), 1)
        self.assertEqual(lruCache.getValueFromKey("b"), 2)
        self.assertEqual(lruCache.getValueFromKey("c"), 3)
        self.assertEqual(lruCache.getValueFromKey("d"), 4)
        lruCache.insertKeyValuePair("e", 5)
        self.assertEqual(lruCache.getValueFromKey("a"), None)
        self.assertEqual(lruCache.getValueFromKey("b"), 2)
        self.assertEqual(lruCache.getValueFromKey("c"), 3)
        self.assertEqual(lruCache.getValueFromKey("d"), 4)
        self.assertEqual(lruCache.getValueFromKey("e"), 5)

    def test_case_4(self):
        lruCache = LRUCache(4)
        lruCache.insertKeyValuePair("a", 1)
        self.assertEqual(lruCache.getMostRecentKey(), "a")
        lruCache.insertKeyValuePair("b", 2)
        self.assertEqual(lruCache.getMostRecentKey(), "b")
        lruCache.insertKeyValuePair("c", 3)
        self.assertEqual(lruCache.getMostRecentKey(), "c")
        lruCache.insertKeyValuePair("d", 4)
        self.assertEqual(lruCache.getMostRecentKey(), "d")
        self.assertEqual(lruCache.getValueFromKey("a"), 1)
        self.assertEqual(lruCache.getMostRecentKey(), "a")
        self.assertEqual(lruCache.getValueFromKey("b"), 2)
        self.assertEqual(lruCache.getMostRecentKey(), "b")
        self.assertEqual(lruCache.getValueFromKey("c"), 3)
        self.assertEqual(lruCache.getMostRecentKey(), "c")
        self.assertEqual(lruCache.getValueFromKey("d"), 4)
        self.assertEqual(lruCache.getMostRecentKey(), "d")
        lruCache.insertKeyValuePair("e", 5)
        self.assertEqual(lruCache.getMostRecentKey(), "e")

    def test_case_5(self):
        lruCache = LRUCache(4)
        lruCache.insertKeyValuePair("a", 1)
        lruCache.insertKeyValuePair("b", 2)
        lruCache.insertKeyValuePair("c", 3)
        lruCache.insertKeyValuePair("d", 4)
        self.assertEqual(lruCache.getValueFromKey("a"), 1)
        lruCache.insertKeyValuePair("e", 5)
        self.assertEqual(lruCache.getValueFromKey("a"), 1)
        self.assertEqual(lruCache.getValueFromKey("b"), None)
        self.assertEqual(lruCache.getValueFromKey("c"), 3)
        lruCache.insertKeyValuePair("f", 5)
        self.assertEqual(lruCache.getValueFromKey("c"), 3)
        self.assertEqual(lruCache.getValueFromKey("d"), None)
        lruCache.insertKeyValuePair("g", 5)
        self.assertEqual(lruCache.getValueFromKey("e"), None)
        self.assertEqual(lruCache.getValueFromKey("a"), 1)
        self.assertEqual(lruCache.getValueFromKey("c"), 3)
        self.assertEqual(lruCache.getValueFromKey("f"), 5)
        self.assertEqual(lruCache.getValueFromKey("g"), 5)

