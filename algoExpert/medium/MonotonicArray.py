# Solution 1
# O(n) time | O(1) space
def isMonotonic(array):
    is_non_increasing = True
    is_non_decreasing = True
    for i in range(1, len(array)):
        if array[i] > array[i - 1]:
            is_non_increasing = False
        elif array[i] < array[i - 1]:
            is_non_decreasing = False
        if not is_non_increasing and not is_non_decreasing:
            return False
    return is_non_increasing or is_non_decreasing


if __name__ == '__main__':
    assert isMonotonic([-1, -5, -10, -1100, -1100, -1101, -1102, -9001]) is True
    assert isMonotonic([1, 5, 10, 1100, 1100, 1101, 1102, 9001]) is True
    assert isMonotonic([1, 5, 10, 1100, 1100, 1101, 1100, 9001]) is False
    assert isMonotonic([1, 5, 10, 1100, 1100, 1101, 1102, 1101]) is False
    assert isMonotonic([-1, -5, -10, -1100, -1100, -1101, -1100, -9001]) is False
    assert isMonotonic([-1, -5, -10, -1100, -1100, -1101, -1102, -1101]) is False
    assert isMonotonic([5, 5, 5, 5, 5, 5, 5, 5]) is True
    assert isMonotonic([1, 5]) is True
    assert isMonotonic([-1]) is True
    assert isMonotonic([]) is True
