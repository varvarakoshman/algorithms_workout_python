import unittest


# optimal solution - (resulting array doesn't count as extra space)
# O(n) time | O(1) space
class Solution:
    def productExceptSelf(self, nums):
        answer = [1] * len(nums)
        for i in range(1, len(nums)):
            answer[i] = answer[i - 1] * nums[i - 1]
        right_product = 1
        for i in range(len(nums) - 1, -1, -1):
            answer[i] = answer[i] * right_product
            right_product *= nums[i]
        return answer


# O(n) time | O(n) space
def productExceptSelf(nums):
    prefix = get_prefix(nums)
    postfix = get_postfix(nums)

    products_except_self = [postfix[1]]
    for i in range(1, len(nums) - 1):
        products_except_self.append(prefix[i - 1] * postfix[i + 1])
    products_except_self.append(prefix[len(nums) - 2])

    return products_except_self


def get_prefix(nums):
    product = 1
    prefix = []
    for i in range(len(nums)):
        product *= nums[i]
        prefix.append(product)
    return prefix


def get_postfix(nums):
    postfix = [0] * len(nums)
    product = 1
    for i in range(len(nums) - 1, -1, -1):
        product *= nums[i]
        postfix[i] = product
    return postfix


# # O(n) time | O(n) space
# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         left_products = self.get_left_products(nums)
#         right_products = self.get_right_products(nums)
#
#         answer = []
#         for i in range(len(nums)):
#             answer.append(left_products[i] * right_products[i])
#         return answer
#
#
#     def get_left_products(self, nums):
#         left_products = [1] * len(nums)
#         for i in range(1, len(nums)):
#             left_products[i] = left_products[i - 1] * nums[i - 1]
#         return left_products
#
#
#     def get_right_products(self, nums):
#         right_products = [1] * len(nums)
#         for i in range(len(nums) - 2, -1, -1):
#             right_products[i] = right_products[i + 1] * nums[i + 1]
#         return right_products


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = [1, 2, 3, 4]
        expected = [24, 12, 8, 6]
        actual = productExceptSelf(input)
        self.assertEqual(expected, actual)

    def test_case_2(self):
        input = [-1, 1, 0, -3, 3]
        expected = [0, 0, 9, 0, 0]
        actual = productExceptSelf(input)
        self.assertEqual(expected, actual)

    def test_case_3(self):
        input = [4, 3, 2, 1, 2]
        expected = [12, 16, 24, 48, 24]
        actual = productExceptSelf(input)
        self.assertEqual(expected, actual)
