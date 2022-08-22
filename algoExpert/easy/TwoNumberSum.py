def two_number_sum(array, targetSum):
    diff_map = {}
    for elem in array:
        if elem in diff_map.keys():
            return [elem, diff_map[elem]]
        else:
            diff_map[targetSum - elem] = elem
    return []

    # complexity: O(n)
    # space complexity: O(n)


if __name__ == '__main__':
    assert two_number_sum([3, 5, -4, 8, 11, 1, -1, 6], 10) == [-1, 11]
    assert two_number_sum([4, 6], 10) == [6, 4]
    assert two_number_sum([4, 6, 1], 5) == [1, 4]
    assert two_number_sum([1], 1) == []