# Solution 1
# O(n) time | O(n) space
def arrayOfProducts_1(array):
    result = []
    left_products = [1] * len(array)
    right_products = [1] * len(array)
    for i in range(len(right_products) - 2, -1, -1):
        right_products[i] = right_products[i + 1] * array[i + 1]
    for i in range(1, len(left_products)):
        left_products[i] = left_products[i - 1] * array[i - 1]
    for i in range(len(array)):
        result.append(left_products[i] * right_products[i])
    return result


# Solution 1.2 (slightly optimized - no extra array)
# O(n) time | O(n) space
def arrayOfProducts(array):
    products = [1] * len(array)
    # [5, 1, 4, 2]
    left_running_product = 1
    for i in range(len(products)):
        products[i] = left_running_product
        left_running_product *= array[i]
    # products = [1, 5, 5, 20]
    right_running_product = 1
    for i in reversed(range(len(array))):
        products[i] *= right_running_product
        right_running_product *= array[i]
    # products = [8, 40, 10, 20]
    return products


if __name__ == '__main__':
    assert arrayOfProducts([5, 1, 4, 2]) == [8, 40, 10, 20]
    assert arrayOfProducts([2, 3]) == [3, 2]
    assert arrayOfProducts([1, 1, 1, 1]) == [1, 1, 1, 1]
    assert arrayOfProducts([-5, -1, 4, 2]) == [-8, -40, 10, 20]
    assert arrayOfProducts([-5, 0, 4, 2]) == [0, -40, 0, 0]
