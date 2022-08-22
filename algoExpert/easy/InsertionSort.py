def insertion_sort(array):
    for index in range(1, len(array)):
        inner_index = index - 1
        while inner_index >= 0:
            if array[index] < array[inner_index]:
                swap(array, index, inner_index)
                index = inner_index
            inner_index -= 1
    return array


def swap(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp

    # complexity: O(n^2)
    # space complexity: O(1)


if __name__ == '__main__':
    assert insertion_sort([8, 5, 2, 9, 5, 6, 3]) == [2, 3, 5, 5, 6, 8, 9]
    assert insertion_sort([4, 3, 2, 1]) == [1, 2, 3, 4]
    assert insertion_sort([1, 2, 3, 4]) == [1, 2, 3, 4]
    assert insertion_sort([1, 5, 4]) == [1, 4, 5]
    assert insertion_sort([1]) == [1]
    assert insertion_sort([]) == []