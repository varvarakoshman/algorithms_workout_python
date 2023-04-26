brackets_pairs = {
    ")": "(",
    "}": "{",
    "]": "[",
}


# O(n) time | O(n) space
def isValid(s):
    stack = []
    for bracket in s:
        if bracket not in brackets_pairs:
            stack.append(bracket)
        elif len(stack) == 0 or brackets_pairs[bracket] != stack.pop():
            return False
    return len(stack) == 0


if __name__ == '__main__':
    assert isValid("()") is True
    assert isValid("())") is False
    assert isValid("()[]{}") is True
    assert isValid("([{}])") is True
    assert isValid("([{)]}") is False
    assert isValid("(]") is False
    assert isValid("(])") is False
    assert isValid("((((") is False
    assert isValid(")))))))") is False
    assert isValid("{") is False
