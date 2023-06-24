# O(n*logn) time | O(n) space
class Solution1:
    def countBits(self, n):
        result = [0] * (n + 1)
        for i in range(n + 1):
            result[i] = self.get_ones_count(i)
        return result

    def get_ones_count(self, n):
        ones_count = 0
        while n > 0:
            ones_count += n % 2
            n = n // 2
        return ones_count


# Improved solution
# O(n) time | O(n) space
class Solution2:
    def countBits(self, n):
        result = [0] * (n + 1)
        for i in range(n + 1):
            result[i] = i % 2 + result[i // 2]
        return result


# Input: n = 5
# Output: [0,1,1,2,1,2]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# 3 --> 11
# 4 --> 100
# 5 --> 101
if __name__ == '__main__':
    solutions = [Solution1(), Solution2()]
    for solution in solutions:
        assert solution.countBits(2) == [0, 1, 1]
        assert solution.countBits(5) == [0, 1, 1, 2, 1, 2]
        assert solution.countBits(1) == [0, 1]
        assert solution.countBits(7) == [0, 1, 1, 2, 1, 2, 2, 3]
