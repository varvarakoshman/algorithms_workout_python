# Solution
# O(n) time | O(1) space
def longest_peak(array):
    max_peak_len = 0
    if len(array) < 3:
        return max_peak_len
    index = 1
    while index < len(array) - 1:
        is_peak = array[index - 1] < array[index] and array[index] > array[index + 1]
        if not is_peak:
            index += 1
            continue

        curr_len = 3
        counter_left = index - 1
        counter_right = index + 1
        while counter_left > 0 and array[counter_left] > array[counter_left - 1]:
            curr_len += 1
            counter_left -= 1
        while counter_right < len(array) - 1 and array[counter_right] > array[counter_right + 1]:
            curr_len += 1
            counter_right += 1

        max_peak_len = max(max_peak_len, curr_len)
        index = counter_right
    return max_peak_len


# Generalization of a solution to find maximum peak len (for both max and min peaks)
# def longest_peak_generalized(array):
#     if len(array) < 3:
#         return 0
#     max_peak_len = 0
#     for i in range(1, len(array) - 1):
#         if check_is_peak(array, i):
#             curr_peak_len = get_peak_len(array, i)
#             max_peak_len = max(max_peak_len, curr_peak_len)
#     return max_peak_len
#
#
# def check_is_peak(array, index):
#     is_max = array[index - 1] < array[index] and array[index] > array[index + 1]
#     is_min = array[index - 1] > array[index] and array[index] < array[index + 1]
#     return is_min or is_max
#
#
# def get_peak_len(array, index):
#     curr_len = 3
#
#     sign_left = get_sign(array[index], array[index - 1])
#     left_index = index - 1
#     while left_index >= 0:
#         curr_sign = get_sign(array[left_index], array[left_index - 1])
#         if curr_sign == sign_left:
#             curr_len += 1
#             left_index -= 1
#         else:
#             break
#
#     sign_right = get_sign(array[index], array[index + 1])
#     right_index = index + 1
#     while right_index < len(array) - 1:
#         curr_sign = get_sign(array[right_index], array[right_index + 1])
#         if curr_sign == sign_right:
#             curr_len += 1
#             right_index += 1
#         else:
#             break
#     return curr_len
#
#
# def get_sign(elem1, elem2):
#     delta = elem1 - elem2
#     if delta > 0:
#         return 1
#     elif delta < 0:
#         return -1
#     else:
#         return 0


if __name__ == '__main__':
    assert longest_peak([1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]) == 6  # 0, 10, 6, 5, -1, -3
    assert longest_peak([-10, -5, 0, -1, 2, 3]) == 4  # -10, -5, 0, -1
    assert longest_peak([1, 2, 3, 2, -10, -5, 0, -1]) == 5  # 1, 2, 3, 2 and -10, -5, 0, -1
    assert longest_peak([1, 2, 3, 2, -10, -5, 0, -1, -2]) == 5
    assert longest_peak([1, 2, 3, 3, 1]) == 0
    assert longest_peak([1, 1, 2, 1, 1]) == 3
    assert longest_peak([]) == 0

    # [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
    # [-, 1, 1, 0, 1, -1, 1, -1, -1, -1, -1, 1, 1]
