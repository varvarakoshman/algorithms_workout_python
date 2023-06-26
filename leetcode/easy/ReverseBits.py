# O(32) ~ O(1) time | O(32) ~ O(1) space
class Solution:
    def reverseBits(self, n: int) -> int:
        resulting_number = 0
        order = 31
        for _ in range(order, -1, -1):
            resulting_number = resulting_number << 1
            bit = n % 2
            resulting_number += bit
            n = n >> 1
        return resulting_number


# if __name__ == '__main__':
#     solution = Solution()
#     assert solution.reverseBits(10100101000001111010011100) == 964176192  # 111001011110000010100101000000
#     assert solution.reverseBits(11111111111111111111111111111101) == 3221225471  # 10111111111111111111111111111111
