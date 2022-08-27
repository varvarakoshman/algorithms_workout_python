# Solution 1
def is_valid_subsequence(array, sequence):
    pointer_array = 0
    pointer_seq = 0
    while pointer_seq < len(sequence) and pointer_array < len(array):
        if sequence[pointer_seq] == array[pointer_array]:
            pointer_seq += 1
        pointer_array += 1
    return pointer_seq == len(sequence)

    # complexity: O(n)
    # space complexity: O(1)


# Solution 2
def is_valid_subsequence_2(array, sequence):
    pointer_seq = 0
    for elem in array:
        if elem == sequence[pointer_seq]:
            pointer_seq += 1
        if pointer_seq == len(sequence):
            return True
    return False


if __name__ == '__main__':
    assert is_valid_subsequence([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10]) is True
    assert is_valid_subsequence([5, 1, 22, 25, 6, -1, 8, 10], [5, 1, 22, 25, 6, -1, 8, 10]) is True
    assert is_valid_subsequence([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, 10]) is True
    assert is_valid_subsequence([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 5]) is False
    assert is_valid_subsequence([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, -1]) is False
    assert is_valid_subsequence([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, -2]) is False
