def binary_search(array, target):
    left = 0
    right = len(array) - 1
    while left <= right:
        middle = (left + right) // 2
        potential_match = array[middle]
        if target == potential_match:
            return middle
        if target > potential_match:
            left = middle + 1
        else:
            right = middle - 1
    return -1

    # complexity: O(logN)
    # space complexity: O(1)


if __name__ == '__main__':
    assert binary_search([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 33) == 3
    assert binary_search([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 73) == 9
    assert binary_search([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 0) == 0
    assert binary_search([1], 1) == 0
    assert binary_search([1], 0) == -1
    assert binary_search([], 1) == -1
    assert binary_search([1, 5], 5) == 1
    assert binary_search([3, 4, 5], 4) == 1
    assert binary_search([3, 4, 5, 6], 5) == 2
