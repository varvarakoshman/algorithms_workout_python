# [8, 5, 2, 9, 5, 6, 3] - iterate backwards and insert each new number
# into an already sorted list at the start
# [[8], 5, 2, 9, 5, 6, 3]
# [[5, 8], 2, 9, 5, 6, 3]
# [[2, 5, 8], 9, 5, 6, 3]
# [[2, 5, 8, 9], 5, 6, 3] ...
def insertion_sort(array):
    for idx in range(1, len(array)):
        while idx > 0 and array[idx] < array[idx - 1]:
            swap(array, idx - 1, idx)
            idx -= 1
    return array


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]

    # complexity: O(n^2)
    # space complexity: O(1)


if __name__ == '__main__':
    assert insertion_sort([8, 5, 2, 9, 5, 6, 3]) == [2, 3, 5, 5, 6, 8, 9]
    assert insertion_sort([4, 3, 2, 1]) == [1, 2, 3, 4]
    assert insertion_sort([1, 2, 3, 4]) == [1, 2, 3, 4]
    assert insertion_sort([1, 5, 4]) == [1, 4, 5]
    assert insertion_sort([1]) == [1]
    assert insertion_sort([]) == []