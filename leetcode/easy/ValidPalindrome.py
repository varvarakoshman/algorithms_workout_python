# O(n) time | O(1) space
def isPalindrome(s):
    if len(s) == 1:
        return True
    left, right = 0, len(s) - 1
    while left < right:
        if not is_alpha_num(s[left]):
            left += 1
        elif not is_alpha_num(s[right]):
            right -= 1
        elif s[left].lower() != s[right].lower():
            return False
        else:
            left += 1
            right -= 1
    return True


def is_alpha_num(char):
    return (ord('A') <= ord(char) <= ord('Z') or
            ord('a') <= ord(char) <= ord('z') or
            ord('0') <= ord(char) <= ord('9'))

# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         left, right = 0, len(s) - 1
#         while left < right:
#             left_char = s[left].lower()
#             right_char = s[right].lower()
#             if not left_char.isalnum():
#                 left += 1
#             elif not right_char.isalnum():
#                 right -= 1
#             elif left_char == right_char:
#                 left += 1
#                 right -= 1
#             else:
#                 return False
#         return True


if __name__ == '__main__':
    assert isPalindrome("A man, a plan, a canal: Panama") is True
    assert isPalindrome("race a car") is False
    assert isPalindrome(" ") is True
    assert isPalindrome("+- +`` `!!_ _") is True
    assert isPalindrome("a1b2c _c2b1a!") is True
    assert isPalindrome("a1b2c _cba!___") is False
    assert isPalindrome("   a1b2c _c2 b1a!n ") is False
    assert isPalindrome("aaba____") is False
