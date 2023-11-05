# Solution 1
# O(n) time | O(1) space
# NB: Boyer–Moore majority vote algorithm
def majorityElement(array):
    major = None
    count = 0
    for num in array:
        if count == 0:
            major = num
        if num == major:
            count += 1
        else:
            count -= 1
    return major


# Solution 2
# O(32*n) ~ O(n) time | O(1) space
# with bitwise operations
def majorityElement_2(array):
    major = 0

    for current_bit in range(32):
        current_bit_value = 1 << current_bit
        ones_count = 0

        for num in array:
            if (num & current_bit_value) != 0:
                ones_count += 1

        if ones_count > len(array) / 2:
            major += current_bit_value

    return major


if __name__ == '__main__':
    assert majorityElement([1, 2, 3, 2, 2, 1, 2]) == 2
