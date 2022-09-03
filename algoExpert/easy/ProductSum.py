# Tip: You can use the type(element) function to check whether an item
# is a list or an integer.
def product_sum(array):
    return product_sum_recursive(array, 1)


def product_sum_recursive(array, depth):
    inner_sum = 0
    for elem in array:
        if type(elem) == int:
            inner_sum += elem
        else:
            # inner_sum += (depth + 1) * product_sum_recursive(elem, depth + 1)
            inner_sum += product_sum_recursive(elem, depth + 1)
    # return inner_sum
    return depth * inner_sum

    # complexity: O(n)
    # space complexity: O(d), d - greatest depth of "special" arrays in an array


if __name__ == '__main__':
    # 5 + 2 + 2 * (7 - 1) + 3 + 2 * (6 + 3 * (-13 + 8) + 4) = 12
    assert product_sum([5, 2, [7, -1], 3, [6, [-13, 8], 4]]) == 12
    # 5 + 2 + 7 + 4 = 18
    assert product_sum([5, 2, 7, 4]) == 18
    # 5 + 2 * 5 + 3 * 5 + 4 * 5 = 50
    assert product_sum([5, [5, [5, [5]]]]) == 165
    assert product_sum([]) == 0
    assert product_sum([10]) == 10
    assert product_sum([[[[5], 5], 5], 5]) == 165
