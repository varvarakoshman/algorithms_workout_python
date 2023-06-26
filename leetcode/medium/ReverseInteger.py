# O(32) ~ O(1) time | O(32) ~ O(1) space
class Solution:
    def reverse(self, x: int) -> int:
        lower_bound, upper_bound = -2 ** 31, 2 ** 31 - 1
        lower_bound_before, upper_bound_before = lower_bound // 10, upper_bound // 10
        lower_bound_latest, upper_bound_latest = lower_bound % 10, upper_bound % 10

        reversed_x = 0
        sign = self.sign(x)
        x = x * sign
        while x != 0:
            latest = x % 10
            x = x // 10
            if reversed_x > upper_bound_before or reversed_x < lower_bound_before or \
                (reversed_x == upper_bound_before and latest > upper_bound_latest) or \
                (reversed_x == lower_bound_before and latest > lower_bound_latest):
                return 0
            reversed_x = reversed_x * 10 + latest
        return reversed_x * sign

    def sign(self, n):
        return 1 if n > 0 else -1


if __name__ == '__main__':
    solution = Solution()
    assert solution.reverse(123) == 321
    assert solution.reverse(-123) == -321
    assert solution.reverse(120) == 21
    assert solution.reverse(0) == 0
    assert solution.reverse(10000) == 1
    assert solution.reverse(1534236469) == 0
    assert solution.reverse(-1534236461) == -1646324351

# Ex:
# 1534236469
# 1011011011100101001011100110101 (31 digits)

# 9646324351
# 1000111110111101110011101001111111 (34 digits)
# (exceeds a 32-bit range)
