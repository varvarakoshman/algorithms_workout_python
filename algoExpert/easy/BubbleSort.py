def bubble_sort(array):
    for current_index in range(len(array)):
        for index in range(len(array)):
            if current_index == index:
                continue
            if array[current_index] < array[index]:
                temp = array[index]
                array[index] = array[current_index]
                array[current_index] = temp
    return array

    # complexity: O(N^2)
    # space complexity: O(1)


if __name__ == '__main__':
    assert bubble_sort([8, 5, 2, 9, 5, 6, 3]) == [2, 3, 5, 5, 6, 8, 9]
    assert bubble_sort([4, 3, 2, 1]) == [1, 2, 3, 4]
    assert bubble_sort([1, 2, 3, 4]) == [1, 2, 3, 4]
    assert bubble_sort([1, 5, 4]) == [1, 4, 5]
    assert bubble_sort([1]) == [1]
    assert bubble_sort([]) == []
