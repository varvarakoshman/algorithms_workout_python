def is_palindrome(string):
    middle = len(string) // 2
    last_index = len(string) - 1
    for i in range(middle):
        if string[i] != string[last_index - i]:
            return False
    return True


if __name__ == '__main__':
    assert is_palindrome("abcdcba") == True
    assert is_palindrome("aaaa") == True
    assert is_palindrome("abccba") == True
    assert is_palindrome("a") == True
    assert is_palindrome("") == True
    assert is_palindrome("ababbaba") == True
    assert is_palindrome(" aaa") == False
