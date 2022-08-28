# Solution 1
def sorted_squared_array(array):
    squared_array = []
    if array[0] >= 0:
        first_positive_index = 0
    else:
        first_positive_index = get_first_positive_index(array)
    right_pointer = first_positive_index
    left_pointer = first_positive_index - 1
    while len(squared_array) < len(array):
        if left_pointer < 0 or right_pointer < len(array) and abs(array[left_pointer]) >= abs(array[right_pointer]):
            squared_array.append(array[right_pointer] ** 2)
            if right_pointer >= 0:
                right_pointer += 1
            else:
                right_pointer -= 1
        else:
            squared_array.append(array[left_pointer] ** 2)
            left_pointer -= 1
    return squared_array


def get_first_positive_index(array):
    for index, elem in enumerate(array):
        if elem > 0:
            return index
    return -1

    # complexity: O(n)
    # space complexity: O(n)


# Solution 1.2 (a shorter & cleaner version!)
def sorted_squared_array_2(array):
    squared_array = [0 for _ in range(len(array))]
    left_pointer = 0
    right_pointer = len(squared_array) - 1
    for idx in reversed(range(len(squared_array))):
        if abs(array[left_pointer]) > abs(array[right_pointer]):
            squared_array[idx] = array[left_pointer] ** 2
            left_pointer += 1
        else:
            squared_array[idx] = array[right_pointer] ** 2
            right_pointer -= 1
    return squared_array

    # complexity: O(n)
    # space complexity: O(n)


# Solution 2 (brute force)
def sortedSquaredArray(array):
    squared_array = []
    for elem in array:
        squared_array.append(elem ** 2)
    return sorted(squared_array)

    # complexity: O(n * log(n))
    # space complexity: O(n)


if __name__ == '__main__':
    assert sorted_squared_array([1, 2, 3]) == [1, 4, 9]
    assert sorted_squared_array([-3, -2, -1]) == [1, 4, 9]
    assert sorted_squared_array([0, 0, 0]) == [0, 0, 0]
    assert sorted_squared_array([-6, 1, 2, 3]) == [1, 4, 9, 36]
    assert sorted_squared_array([-5, -3, 2, 4]) == [4, 9, 16, 25]
    assert sorted_squared_array([-5, -3, 2, 4, 6]) == [4, 9, 16, 25, 36]
    assert sorted_squared_array([-7, -5, -3, 4, 6]) == [9, 16, 25, 36, 49]
    assert sorted_squared_array([-11, -2, -1, 0]) == [0, 1, 4, 121]
