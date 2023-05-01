# TODO: add complexity analysis
class Solution(object):
    def generateParenthesis(self, k):
        resulting_sequence, curr_stack = [], []
        opened_count = 0
        generate_parenthesis_helper(resulting_sequence, curr_stack, opened_count, k)
        return resulting_sequence


def generate_parenthesis_helper(resulting_sequence, curr_stack, opened_count, k):
    if len(curr_stack) == 2 * k:
        resulting_sequence.append(''.join(curr_stack))
        return
    if opened_count < k:
        curr_stack.append("(")
        generate_parenthesis_helper(resulting_sequence, curr_stack, opened_count + 1, k)
        curr_stack.pop()
    if opened_count * 2 > len(curr_stack):
        curr_stack.append(")")
        generate_parenthesis_helper(resulting_sequence, curr_stack, opened_count, k)
        curr_stack.pop()


if __name__ == '__main__':
    assert Solution().generateParenthesis(3) == ["((()))", "(()())", "(())()", "()(())", "()()()"]
    assert Solution().generateParenthesis(1) == ["()"]
