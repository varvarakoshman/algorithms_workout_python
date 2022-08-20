def isPalindrome(string):
    middle = len(string) // 2
    last_index = len(string) - 1
    for i in range(middle):
        if string[i] != string[last_index - i]:
            return False
    return True


if __name__ == '__main__':
    assert isPalindrome("abcdcba") == True
    assert isPalindrome("aaaa") == True
    assert isPalindrome("abccba") == True
    assert isPalindrome("a") == True
    assert isPalindrome("") == True
    assert isPalindrome("ababbaba") == True
    assert isPalindrome(" aaa") == False
