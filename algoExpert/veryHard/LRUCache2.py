import unittest


class LRUCache:
    def __init__(self, max_size):
        self.maxSize = max_size or 1
        self.cache = {}
        self.listOfMostRecent = DoublyLinkedList()
        self.currentSize = 0

    # O(1) time | O(1) space
    def insertKeyValuePair(self, key, value):
        if key not in self.cache:
            if self.currentSize == self.maxSize:
                self.evictLeastRecent()
            else:
                self.currentSize += 1
            self.cache[key] = DoublyLinkedListNode(key, value)
        else:
            self.replaceKey(key, value)
        self.updateMostRecent(self.cache[key])

    # O(1) time | O(1) space
    def getValueFromKey(self, key):
        if key not in self.cache:
            return None
        self.updateMostRecent(self.cache[key])
        return self.cache[key].value

    # O(1) time | O(1) space
    def getMostRecentKey(self):
        return self.listOfMostRecent.head.key if self.listOfMostRecent.head else None

    def evictLeastRecent(self):
        keyToRemove = self.listOfMostRecent.tail.key
        self.listOfMostRecent.removeTail()
        del self.cache[keyToRemove]

    def updateMostRecent(self, node):
        self.listOfMostRecent.setHeadTo(node)

    def replaceKey(self, key, value):
        if key not in self.cache:
            raise Exception("The provided key isn't in the cache!")
        self.cache[key].value = value


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def setHeadTo(self, node):
        if self.head == node:
            return
        elif not self.head:
            self.head = node
            self.tail = node
        elif self.head == self.tail:
            self.tail.prev = node
            self.head = node
            self.head.next = self.tail
        else:
            if self.tail == node:
                self.removeTail()
            node.removeBindings()
            self.head.prev = node
            node.next = self.head
            self.head = node

    def removeTail(self):
        if self.tail == self.head:
            self.tail = None
            self.head = None
            return
        self.tail = self.tail.prev
        self.tail.next = None


class DoublyLinkedListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

    def removeBindings(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev
        self.prev = None
        self.next = None


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
