# Solution 1 (brute force approach) - O(n^2) time | O(1) space
def smallest_difference_1(arrayOne, arrayTwo):
    smallest_diff = float("inf")
    optimal_pair = []
    for first in arrayOne:
        for second in arrayTwo:
            current_diff = abs(first - second)
            if current_diff < smallest_diff:
                smallest_diff = current_diff
                optimal_pair = [first, second]
    return optimal_pair


# Solution 2 (optimal approach) - O(nlog(n) + mlog(m)) time | O(1) space
def smallest_difference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    pointer_one, pointer_two = 0, 0
    smallest_diff = float("inf")
    optimal_pair = []
    while pointer_one < len(arrayOne) and pointer_two < len(arrayTwo):
        first_num = arrayOne[pointer_one]
        second_num = arrayTwo[pointer_two]
        current_diff = abs(first_num - second_num)
        if first_num < second_num:
            pointer_one += 1
        elif second_num < first_num:
            pointer_two += 1
        else:
            return [first_num, second_num]
        if current_diff < smallest_diff:
            smallest_diff = current_diff
            optimal_pair = [first_num, second_num]
    return optimal_pair


if __name__ == '__main__':
    assert smallest_difference([-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17]) == [28, 26]  # 2
    assert smallest_difference([1, 2, 3, 4], [4, 3, 2, 1]) == [1, 1]  # 0
    assert smallest_difference([8, 8, 8], [8, 8, 8, 8]) == [8, 8]  # 0
    assert smallest_difference([5], [22]) == [5, 22]  # 18
    assert smallest_difference([-5, 4], [-4, -5, -5]) == [-5, -5]  # 1
    assert smallest_difference([-5, 4], [-10, 14, -3]) == [-5, -3]  # 2
    assert smallest_difference([1, -2, -3, 4, -4], [-4, 3, 2]) == [-4, -4]  # 0
    assert smallest_difference([10, 0, 20, 25, 2000], [1005, 1006, 1014, 1032, 1031]) == [2000, 1032]  # 0

#     [-5, 4],
#     [-10, -3, 14]
# ----------------------------------------------------
#    -10       -5    -3           4                 14
#     =         -     =           -                  =
# => [-5, -3]

#     [1, 4],
#     [10, 12, 14]
# ----------------------------------------------------
#    1     4               10   12   14
#    -     -                =    =    =
# => [4, 10]

# min(|arr2[i] - arr1[j]|)
