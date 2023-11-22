from random import choice


class RandomizedSet:

    def __init__(self):
        self.map = {}
        self.elements = []

    # O(1) time | O(1) space
    def insert(self, val: int) -> bool:
        if val in self.map:
            return False
        else:
            self.elements.append(val)
            self.map[val] = len(self.elements) - 1
            return True

    # O(1) time | O(1) space
    def remove(self, val: int) -> bool:
        if val not in self.map:
            return False
        else:
            last_idx = len(self.elements) - 1
            val_to_replace = self.elements[last_idx]
            removing_elem_idx = self.map[val]
            self.elements[removing_elem_idx] = val_to_replace
            self.map[val_to_replace] = removing_elem_idx
            self.elements.pop()
            self.map.pop(val)
            return True

    # O(1) time | O(1) space
    def getRandom(self) -> int:
        return choice(self.elements)


if __name__ == '__main__':
    randomizedSet = RandomizedSet()
    assert randomizedSet.insert(1) is True
    assert randomizedSet.remove(2) is False
    assert randomizedSet.insert(2) is True
    assert randomizedSet.getRandom() in [1, 2]
    assert randomizedSet.remove(1) is True
    assert randomizedSet.insert(2) is False
    assert randomizedSet.getRandom() == 2
