# O(1) time | O(1) space
class Solution:
    def intToRoman(self, num: int) -> str:
        digits = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"),
                  (90, "XC"), (50, "L"), (40, "XL"), (10, "X"), (9, "IX"),
                  (5, "V"), (4, "IV"), (1, "I")]
        roman = []
        for int_value, roman_value in digits:
            if num == 0:
                break
            while num > 0 and num >= int_value:
                num -= int_value
                roman.append(roman_value)
        return "".join(roman)
