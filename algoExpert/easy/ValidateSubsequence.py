def is_valid_subsequence(array, sequence):
    pointer_array = 0
    pointer_seq = 0
    while pointer_seq < len(sequence) and pointer_seq < len(array) and pointer_array < len(array):
        if sequence[pointer_seq] == array[pointer_array]:
            pointer_seq += 1
        pointer_array += 1
    return pointer_seq == len(sequence)

    # complexity: O(n)
    # space complexity: O(1)


if __name__ == '__main__':
    assert is_valid_subsequence([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10]) is True
    assert is_valid_subsequence([5, 1, 22, 25, 6, -1, 8, 10], [5, 1, 22, 25, 6, -1, 8, 10]) is True
    assert is_valid_subsequence([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, 10]) is True
    assert is_valid_subsequence([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 5]) is False
    assert is_valid_subsequence([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, -1]) is False
    assert is_valid_subsequence([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, -2]) is False
