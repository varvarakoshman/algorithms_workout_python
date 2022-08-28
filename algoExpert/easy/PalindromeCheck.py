# Solution 1 - string concatenation (a naive approach)
def is_palindrome_1(string):
    reversed_str = ""
    for idx in reversed(range(len(string))):
        reversed_str += string[idx]
    return reversed_str == string

    # complexity: O(n^2)
    # space complexity: O(n)


# Solution 2 - list concatenation (an improvement of a naive approach)
def is_palindrome_2(string):
    reversed_chars = []
    for idx in reversed(range(len(string))):
        reversed_chars.append(string[idx])
    return ''.join(reversed_chars) == string

    # complexity: O(n)
    # space complexity: O(n)


# Solution 3 - a recursive approach
def is_palindrome_3(string):
    if len(string) == 1 or len(string) == 0:
        return True
    # new string created each time (doesn't affect overall complexity, but still.. 3_2 version is better)
    return string[0] == string[-1] and is_palindrome_3(string[1:-1])

    # complexity: O(n/2) = O(n)
    # space complexity: O(n/2) = O(n)


# Solution 3.1 - a recursive approach
def is_palindrome_3_2(string, start=0):
    end = len(string) - 1 - start
    if start >= end:
        return True
    return string[start] == string[end] and is_palindrome_3_2(string, start + 1)

    # complexity: O(n/2) = O(n)
    # space complexity: O(n/2) = O(n)


# Solution 4 - two pointers (the best one)
def is_palindrome(string):
    middle = len(string) // 2
    last_index = len(string) - 1
    for i in range(middle):
        if string[i] != string[last_index - i]:
            return False
    return True

    # complexity: O(n)
    # space complexity: O(1)


if __name__ == '__main__':
    assert is_palindrome("abcdcba") is True
    assert is_palindrome("aaaa") is True
    assert is_palindrome("abccba") is True
    assert is_palindrome("a") is True
    assert is_palindrome("") is True
    assert is_palindrome("ababbaba") is True
    assert is_palindrome(" aaa") is False
