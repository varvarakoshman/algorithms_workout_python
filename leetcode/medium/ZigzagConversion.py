# O(n) time | O(1) space
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) <= numRows or numRows == 1:
            return s
        result = []
        period = 2 * numRows - 2
        for i in range(numRows - 1):
            result.append(s[i])
            curr_idx = period
            while curr_idx - i < len(s):
                result.append(s[curr_idx - i])
                if i != 0 and curr_idx + i < len(s):
                    result.append(s[curr_idx + i])
                curr_idx += period
        curr_idx = numRows - 1
        while curr_idx < len(s):
            result.append(s[curr_idx])
            curr_idx += period
        return "".join(result)


if __name__ == '__main__':
    solution = Solution()
    assert solution.convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR"
    assert solution.convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI"
    assert solution.convert("A", 1) == "A"
    assert solution.convert("ABCD", 3) == "ABDC"
