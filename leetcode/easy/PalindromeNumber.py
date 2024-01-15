# O(n) time | O(1) space
class Solution1:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        count = self.get_count(x)
        right, left = 0, count - 1
        while left > right:
            left_digit = self.get_digit_by_position(x, left)
            right_digit = self.get_digit_by_position(x, right)
            if left_digit != right_digit:
                return False
            left -= 1
            right += 1
        return True

    def get_count(self, number):
        count = 0
        while number > 0:
            count += 1
            number //= 10
        return count

    def get_digit_by_position(self, number, position):
        return (number // 10 ** position) % 10


# O(n) time | O(1) space
class Solution2:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        reversed = 0
        input = x
        while input > 0:
            reversed = reversed * 10 + input % 10
            input = input // 10
        return x == reversed


# O(n) time | O(1) space
class Solution3:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or x != 0 and x % 10 == 0:
            return False
        reversed = 0
        input = x
        while reversed < input:
            reversed = reversed * 10 + input % 10
            input = input // 10
        return input == reversed or reversed // 10 == input
