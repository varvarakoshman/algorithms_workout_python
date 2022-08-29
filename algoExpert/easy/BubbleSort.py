# [8, 5, 2, 9, 5, 6, 3]
def bubble_sort(array):
    is_sorted = False
    counter = 0
    while not is_sorted:
        is_sorted = True
        for inner_index in range(len(array) - 1 - counter):
            if array[inner_index] > array[inner_index + 1]:
                swap(array, inner_index, inner_index + 1)
                is_sorted = False
        counter += 1
    return array


def swap(array, left, right):
    array[left], array[right] = array[right], array[left]

    # complexity: O(N^2)
    # space complexity: O(1)


if __name__ == '__main__':
    assert bubble_sort([8, 5, 2, 9, 5, 6, 3]) == [2, 3, 5, 5, 6, 8, 9]
    assert bubble_sort([4, 3, 2, 1]) == [1, 2, 3, 4]
    assert bubble_sort([1, 2, 3, 4]) == [1, 2, 3, 4]
    assert bubble_sort([1, 5, 4]) == [1, 4, 5]
    assert bubble_sort([1]) == [1]
    assert bubble_sort([]) == []
