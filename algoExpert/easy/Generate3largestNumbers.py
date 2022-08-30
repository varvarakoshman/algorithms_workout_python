# Solution 1 (brute force)
# just sort the input array and return the last 3 elements - O(n*log(N))

# Solution 2 (optimal)
def find_three_largest_numbers(array):
    output = [float('-inf')] * 3
    for num in array:
        update_largest(output, num)
    return output


# [0, 1, 2]
# [x, y, z]
def shift_output_left(output, right_index, num):
    for i in range(1, right_index):
        output[i - 1] = output[i]
    output[right_index - 1] = num


def update_largest(output, num):
    if num >= output[2]:
        shift_output_left(output, len(output), num)
    elif num >= output[1]:
        shift_output_left(output, len(output) - 1, num)
    elif num >= output[0]:
        output[0] = num

    # complexity: O(n)
    # space complexity: O(1)


if __name__ == '__main__':
    assert find_three_largest_numbers([10, 5, 9, 10, 12]) == [10, 10, 12]
    assert find_three_largest_numbers([1, 2, 3]) == [1, 2, 3]
    assert find_three_largest_numbers([0, 0, 0]) == [0, 0, 0]
    assert find_three_largest_numbers([3, 2, 1]) == [1, 2, 3]
    assert find_three_largest_numbers([1, -10, 1, -5, 0, -3]) == [0, 1, 1]
    assert find_three_largest_numbers([55, 43, 11, 3, -3, 10]) == [11, 43, 55]
    assert find_three_largest_numbers([-1, -2, -3, -7, -17, -27, -18, -541, -8, -7, 7]) == [-2, -1, 7]
    assert find_three_largest_numbers([7, 7, 7, 7, 7, 7, 8, 7, 7, 7, 7]) == [7, 7, 8]
