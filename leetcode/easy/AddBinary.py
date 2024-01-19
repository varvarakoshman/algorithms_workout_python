# O(n) time | O(n) space
# , n = max(len(a), len(b))
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = []
        right_idx_a, right_idx_b = len(a) - 1, len(b) - 1
        carry = 0
        while right_idx_a >= 0 or right_idx_b >= 0:
            a_right = int(a[right_idx_a]) if right_idx_a >= 0 else 0
            b_right = int(b[right_idx_b]) if right_idx_b >= 0 else 0
            curr_sum = a_right + b_right + carry
            if curr_sum == 2:
                carry = 1
                result.append('0')
            elif curr_sum == 3:
                carry = 1
                result.append('1')
            else:
                carry = 0
                result.append(str(curr_sum))
            if right_idx_a >= 0:
                right_idx_a -= 1
            if right_idx_b >= 0:
                right_idx_b -= 1
        if carry == 1:
            result.append('1')
        result.reverse()
        return ''.join(result)
