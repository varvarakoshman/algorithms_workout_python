# Solution 1 - with in-place sorting
# O(n*logn) time | O(1) space
def move_element_to_end_1(array, toMove):
    array.sort()
    start_index = -1
    end_index = len(array) - 1
    for i in range(len(array)):
        if array[i] == toMove and start_index == -1:
            start_index = i
        elif array[i - 1] == toMove:
            end_index = i - 1
    if start_index == -1:
        return array
    for i in range(end_index + 1, len(array)):
        array[start_index] = array[i]
        array[i] = toMove
        start_index += 1
    return array


# Solution 2 (optimal)
# O(n) time | O(1) space
def move_element_to_end(array, toMove):
    right_border = get_right_border(array, toMove, 0, len(array) - 1)
    index = 0
    while index < right_border:
        if array[index] == toMove:
            array[index], array[right_border] = array[right_border], toMove
            right_border = get_right_border(array, toMove, index, right_border - 1)
        index += 1
    return array


def get_right_border(array, toMove, start, end):
    for i in range(end, start - 1, -1):
        if array[i] != toMove:
            return i
    return 0

# Model answer
# def move_element_to_end(array, toMove):
#     left_index = 0
#     right_index = len(array) - 1
#     while left_index < right_index:
#         while left_index < right_index and array[right_index] == toMove:
#             right_index -= 1
#         if array[left_index] == toMove:
#             array[left_index], array[right_index] = array[right_index], toMove
#         left_index += 1
#     return array


if __name__ == '__main__':
    assert move_element_to_end([2, 1, 2, 2, 2, 3, 4, 2], 2) == [4, 1, 3, 2, 2, 2, 2, 2]
    assert move_element_to_end([3, 3, 3, 3, 3], 3) == [3, 3, 3, 3, 3]
    assert move_element_to_end([1, 1, 3, 2, 1], 1) == [2, 3, 1, 1, 1]
    assert move_element_to_end([3, 2, 1, 1, 1], 1) == [3, 2, 1, 1, 1]
    assert move_element_to_end([1, 2, 3], 1) == [3, 2, 1]
    assert move_element_to_end([1, 2], 1) == [2, 1]
    assert move_element_to_end([3, 3, 3, 3, 3], 4) == [3, 3, 3, 3, 3]
    assert move_element_to_end([1], 1) == [1]
    assert move_element_to_end([], 1) == []
    assert move_element_to_end([5, 1, 2, 5, 5, 3, 4, 6, 7, 5, 8, 9, 10, 11, 5, 5, 12], 5) == \
           [12, 1, 2, 11, 10, 3, 4, 6, 7, 9, 8, 5, 5, 5, 5, 5, 5]
