class Solution(object):
    def evalRPN(self, tokens):
        stack = []
        operators = ['+', '-', '/', '*']
        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                first_value = stack.pop()
                second_value = stack.pop()
                result = self.apply_operator(token, first_value, second_value)
                stack.append(result)
        return stack[-1]

    def apply_operator(self, token, first_value, second_value):
        if token == '+':
            return first_value + second_value
        elif token == '-':
            return second_value - first_value
        elif token == '*':
            return first_value * second_value
        else:
            return int(float(second_value) / first_value)


# 2 1 + 3 *
# ((2 + 1) * 3) = 9

# 4 13 5 / +
# (4 + (13 / 5)) = 6

# 10 6 9 3 + -11 * / * 17 + 5 +
# ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
if __name__ == '__main__':
    assert Solution().evalRPN(["2", "1", "+", "3", "*"]) == 9
    assert Solution().evalRPN(["4", "13", "5", "/", "+"]) == 6
    assert Solution().evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]) == 22
