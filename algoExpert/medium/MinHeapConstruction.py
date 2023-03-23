import unittest


class MinHeap:
    def __init__(self, array):
        self.heap = self.buildHeap(array)

    # O(n) time | O(1) space
    def buildHeap(self, array):
        self.heapify(array)
        return array

    # O(n) time | O(1) space
    def heapify(self, array):
        heap_end_idx = len(array) - 1
        parent_idx = (heap_end_idx - 1) // 2
        while parent_idx >= 0:
            self.siftDown(array, parent_idx, heap_end_idx)
            parent_idx -= 1

    # O(logn) time | O(1) space
    def siftDown(self, array, parent_idx, heap_end_idx):
        left_child = parent_idx * 2 + 1
        while left_child <= heap_end_idx:
            min_child = left_child
            right_child = parent_idx * 2 + 2
            if right_child <= heap_end_idx and array[right_child] < array[left_child]:
                min_child = right_child
            if array[min_child] >= array[parent_idx]:
                break
            array[min_child], array[parent_idx] = array[parent_idx], array[min_child]
            parent_idx = min_child
            left_child = parent_idx * 2 + 1

    # O(logn) time | O(1) space
    def siftUp(self, array, curr_idx):
        parent_idx = (curr_idx - 1) // 2
        while array[curr_idx] < array[parent_idx]:
            array[curr_idx], array[parent_idx] = array[parent_idx], array[curr_idx]
            curr_idx = parent_idx
            parent_idx = (curr_idx - 1) // 2

    # O(1) time | O(1) space
    def peek(self):
        return self.heap[0]

    # O(logn) time | O(1) space
    def remove(self):
        min_elem = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.siftDown(self.heap, 0, len(self.heap) - 1)
        return min_elem

    # O(logn) time | O(1) space
    def insert(self, value):
        self.heap.append(value)
        self.siftUp(self.heap, len(self.heap) - 1)


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        array = [48, 12, 24, 7, 8, -5, 24, 391, 24, 56, 2, 6, 8, 41]
        min_heap = MinHeap(array)
        assert min_heap.heap == [-5, 2, 6, 7, 8, 8, 24, 391, 24, 56, 12, 24, 48, 41]
        min_heap.insert(76)
        assert min_heap.heap == [-5, 2, 6, 7, 8, 8, 24, 391, 24, 56, 12, 24, 48, 41, 76]
        assert min_heap.peek() == -5
        assert min_heap.remove() == -5
        assert min_heap.heap == [2, 7, 6, 24, 8, 8, 24, 391, 76, 56, 12, 24, 48, 41]
        assert min_heap.peek() == 2
        assert min_heap.remove() == 2
        assert min_heap.heap == [6, 7, 8, 24, 8, 24, 24, 391, 76, 56, 12, 41, 48]
        assert min_heap.peek() == 6
        min_heap.insert(87)
        assert min_heap.heap == [6, 7, 8, 24, 8, 24, 24, 391, 76, 56, 12, 41, 48, 87]
