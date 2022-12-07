# Solution 1 - time O(n) | space O(n)
def first_duplicate_value_1(array):
    value_indices = {}
    for index, value in enumerate(array):
        if value not in value_indices:
            value_indices[value] = [index]
        else:
            value_indices[value].append(index)
    min_index = len(array)
    first_duplicate = -1
    for value, indices in value_indices.items():
        if len(indices) > 1 and indices[1] < min_index:
            min_index = indices[1]
            first_duplicate = value
    return -1 if min_index == len(array) else first_duplicate

# Ex: representation for Solution 1:
# 2: [0, 3]
# 1: [1]
# 3: [4, 5]
# 4: [6]
# 5: [2]


# Solution 2 - time O(n*log(n)) | space O(n)
# sort initial array
def first_duplicate_value_2(array):
    indices = [index for index in range(len(array))]
    # [2, 1, 5, 2, 3, 3, 4] - initial array
    # [0, 1, 2, 3, 4, 5, 6] - array of indices
    indices.sort(key=lambda index: array[index])
    array.sort()
    # [1, 2, 2, 3, 3, 4, 5] - sorted initial array
    # [1, 0, 3, 4, 5, 6, 7] - sorted array of indices
    min_index = len(array)
    first_duplicate = -1
    for i in range(1, len(array)):
        if array[i] == array[i - 1] and indices[i] < min_index:
            min_index = indices[i]
            first_duplicate = array[i]
    return -1 if min_index == len(array) else first_duplicate

# Another example:
# [2, 1, 5, 3, 3, 2, 4]
# [0, 1, 2, 3, 4, 5, 6]

# [1, 2, 2, 3, 3, 4, 5]
# [1, 0, 5, 3, 4, 6, 2]


# Solution 3 (optimal) - time O(n) | space O(1)
def first_duplicate_value(array):
    for value in array:
        abs_value = abs(value)
        if array[abs_value - 1] < 0:
            return abs_value
        array[abs_value - 1] *= -1
    return -1


# given integers between 0..n, where n = len(array)
# return the value of the 1st duplicate
if __name__ == '__main__':
    assert first_duplicate_value([2, 1, 5, 2, 3, 3, 4]) == 2
    assert first_duplicate_value([2, 1, 5, 3, 3, 2, 4]) == 3
    assert first_duplicate_value([2, 1, 3, 3, 3, 3, 2, 2]) == 3
    assert first_duplicate_value([1, 2, 3, 4, 5, 5]) == 5
    assert first_duplicate_value([1, 1, 1, 1, 1]) == 1
    assert first_duplicate_value([1, 2, 3, 4, 5, 6]) == -1
    assert first_duplicate_value([5, 5, 5, 4, 6, 6, 2]) == 5
    assert first_duplicate_value([1, 2]) == -1
    assert first_duplicate_value([]) == -1
