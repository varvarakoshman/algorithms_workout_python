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


if __name__ == '__main__':
    assert two_number_sum([3, 5, -4, 8, 11, 1, -1, 6], 10) == [-1, 11]
    assert two_number_sum([4, 6], 10) == [6, 4]
    assert two_number_sum([4, 6, 1], 5) == [1, 4]
    assert two_number_sum([1], 1) == []