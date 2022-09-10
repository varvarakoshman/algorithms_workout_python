# Solution with stack - O(n) time | O(n) space
def balancedBrackets(string):
    brackets = {
        "}": "{",
        "]": "[",
        ")": "("
    }
    opening_brackets = brackets.values()
    closing_brackets = brackets.keys()
    stack = []
    for char in string:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets and (len(stack) == 0 or stack.pop() != brackets[char]):
            return False
    return len(stack) == 0


if __name__ == '__main__':
    assert balancedBrackets("([])(){}(())()()") is True
    assert balancedBrackets("[]{}()") is True
    assert balancedBrackets("a[a]{rr}(u)u") is True
    assert balancedBrackets("[{()}]") is True
    assert balancedBrackets("[s{(d)yy}pp]b") is True
    assert balancedBrackets("[{(){{}}}]") is True
    assert balancedBrackets("[]") is True
    assert balancedBrackets("aaaa") is True
    assert balancedBrackets("") is True
    assert balancedBrackets("aaa){a") is False
    assert balancedBrackets("[(])") is False
    assert balancedBrackets("aaaa}") is False
    assert balancedBrackets("(((a))))") is False
    assert balancedBrackets("({[()]}") is False

    # valid if:
    # 1) number of opening == number of closing
    # 2) each closing is correct (closes last open)

    # [{(){{}}}]
    # [{( {{
    #    )  }}}]
