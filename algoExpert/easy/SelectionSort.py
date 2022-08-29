# [8, 5, 2, 9, 5, 6, 3]
# a sorted and an unsorted sublist
# find a minimum each time and append it to an already sorted sublist
# 1) # [[], 8, 5, 2, 9, 5, 6, 3] - 2 is min => swap with the 1st one in the unsorted part (swap(8, 2))
# => [[2], 5, 8, 9, 5, 6, 3]
# 2) 3 is min => [[2, 3], 8, 9, 5, 6, 5]
# 3) 5 is min => [[2, 3, 5], 9, 8, 6, 5]
# 4) 5 is min => [[2, 3, 5, 5], 8, 6, 9]
# 5) 6 is min => [[2, 3, 5, 5, 6], 8, 9]
# 6) 8 is min => [[2, 3, 5, 5, 6, 8], 9]
# 7) the last one is in it's sorted position => done: [[2, 3, 5, 5, 6, 8, 9]]
# return sorted list
def selection_sort(array):
    end_index = len(array)
    for i in range(end_index):
        min_index = get_min_index(array, i)
        swap(array, min_index, i)
    return array


def get_min_index(array, start):
    min_idex = start
    for i in range(start + 1, len(array)):
        if array[i] < array[min_idex]:
            min_idex = i
    return min_idex


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]

    # complexity: O(n^2)
    # space complexity: O(1)


if __name__ == '__main__':
    assert selection_sort([8, 5, 2, 9, 5, 6, 3]) == [2, 3, 5, 5, 6, 8, 9]
    assert selection_sort([4, 3, 2, 1]) == [1, 2, 3, 4]
    assert selection_sort([1, 2, 3, 4]) == [1, 2, 3, 4]
    assert selection_sort([1, 5, 4]) == [1, 4, 5]
    assert selection_sort([1]) == [1]
    assert selection_sort([]) == []