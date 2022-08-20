def fin_three_largest_numbers(array):
    output = [float('-inf')] * 3
    for num in array:
        update_largest(output, num)
    return output


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


if __name__ == '__main__':
    assert fin_three_largest_numbers([10, 5, 9, 10, 12]) == [10, 10, 12]