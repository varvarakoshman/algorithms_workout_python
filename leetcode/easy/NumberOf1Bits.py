# O(32) ~ O(1) time | O(1) space
class Solution1:
    def hammingWeight(self, n: int) -> int:
        result = 0
        while n > 0:
            result += n % 2
            n = n >> 1
        return result


# O(32) ~ O(1) time | O(1) space
class Solution2:
    def hammingWeight(self, n: int) -> int:
        result = 0
        while n > 0:
            n &= n - 1
            result += 1
        return result


if __name__ == '__main__':
    solutions = [Solution1(), Solution2()]
    for solution in solutions:
        assert solution.hammingWeight(1011) == 3
        assert solution.hammingWeight(10000000) == 1
        assert solution.hammingWeight(11111111111111111111111111111101) == 31
        assert solution.hammingWeight(0) == 0
