# O(n) time | O(n) space
class Solution:
    def plusOne(self, digits):
        result = []
        carry = 0
        for index, digit in enumerate(reversed(digits)):
            curr_sum = digit + carry
            if index == 0:
                curr_sum += 1
            if curr_sum > 9:
                result.append(curr_sum % 10)
                carry = 1
            else:
                result.append(curr_sum)
                carry = 0
        if carry:
            result.append(1)
        return result[::-1]
        # result.reverse()
        # return result


if __name__ == '__main__':
    solution = Solution()
    assert solution.plusOne([4, 3, 2, 1]) == [4, 3, 2, 2]
    assert solution.plusOne([9, 9, 9]) == [1, 0, 0, 0]
    assert solution.plusOne([9]) == [1, 0]
    assert solution.plusOne([9, 7, 9]) == [9, 8, 0]
