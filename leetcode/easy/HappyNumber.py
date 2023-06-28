# O(n*k) time | O(n) space
# n - # of numbers before repeating number occurs, k - max number of digits in iteration
class Solution1:
    def isHappy(self, n: int) -> bool:
        squares = set()
        while n != 1 and n not in squares:
            squares.add(n)
            new_n = 0
            while n > 0:
                new_n += (n % 10) ** 2
                n = n // 10
            n = new_n
        return n == 1


# O(n*k) time | O(1) space
class Solution2:
    def get_digit_squares(self, n):
        new_n = 0
        while n > 0:
            new_n += (n % 10) ** 2
            n = n // 10
        return new_n

    def isHappy(self, n: int) -> bool:
        fast, slow = n, n
        while True:
            slow = self.get_digit_squares(slow)
            fast = self.get_digit_squares(fast)
            fast = self.get_digit_squares(fast)
            if fast == slow:
                break
        slow = n
        while slow != fast:
            slow = self.get_digit_squares(slow)
            fast = self.get_digit_squares(fast)
        return slow == 1


if __name__ == '__main__':
    solutions = [Solution1(), Solution2()]
    for solution in solutions:
        assert solution.isHappy(19) is True
        assert solution.isHappy(2) is False
        assert solution.isHappy(1000) is True
