def selection_sort(array):
    end_index = len(array)
    for i in range(end_index):
        min_index = get_min_index(array, i, end_index)
        swap(array, min_index, i)
    return array


def get_min_index(array, start, end):
    min_elem = array[start]
    min_idex = start
    for i in range(start + 1, end):
        if array[i] < min_elem:
            min_elem = array[i]
            min_idex = i
    return min_idex


def swap(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp

    # complexity: O(n^2)
    # space complexity: O(1)


if __name__ == '__main__':
    assert selection_sort([8, 5, 2, 9, 5, 6, 3]) == [2, 3, 5, 5, 6, 8, 9]
    assert selection_sort([4, 3, 2, 1]) == [1, 2, 3, 4]
    assert selection_sort([1, 2, 3, 4]) == [1, 2, 3, 4]
    assert selection_sort([1, 5, 4]) == [1, 4, 5]
    assert selection_sort([1]) == [1]
    assert selection_sort([]) == []