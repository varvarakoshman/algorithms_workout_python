def two_number_sum(array, targetSum):
    differences = set()
    for elem in array:
        if elem in differences:
            return [elem, targetSum - elem]
        else:
            differences.add(targetSum - elem)
    return []

    # complexity: O(n)
    # space complexity: O(n)


def two_number_sum_2(array, targetSum):
    # target = 10
    # [3, 5, -4, 8, 11, 1, -1, 6] => [-4, -1, 1, 3, 5, 6, 8, 11]
    array.sort()
    left_index = 0
    right_index = len(array) - 1
    while left_index != right_index:
        curr_sum = array[left_index] + array[right_index]
        if curr_sum > targetSum:
            right_index -= 1
        elif curr_sum < targetSum:
            left_index += 1
        else:
            return [array[left_index], array[right_index]]
    return []

    # complexity: O(n * log(n))
    # space complexity: O(1)


if __name__ == '__main__':
    assert two_number_sum_2([3, 5, -4, 8, 11, 1, -1, 6], 10) == [-1, 11]
    assert two_number_sum_2([4, 6], 10) == [4, 6]
    assert two_number_sum_2([4, 6, 1], 5) == [1, 4]
    assert two_number_sum_2([1], 1) == []
