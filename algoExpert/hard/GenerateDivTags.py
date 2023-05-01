import unittest

# number of output string for a given number: (2*n)! / ((n + 1)!*n!)   (Catalan number)
# O((2*n)! / ((n + 1)!*n!)) time
# O((2*n)! / ((n + 1)!*n!)) space
def generateDivTags(number_of_tags):
    resulting_sequence, curr_stack = [], []
    generateDivTags_helper(resulting_sequence, curr_stack, number_of_tags, 0)
    return resulting_sequence


def generateDivTags_helper(resulting_sequence, curr_stack, number_of_tags, number_of_opened):
    if len(curr_stack) == 2 * number_of_tags:
        resulting_sequence.append(''.join(curr_stack))
        return
    if number_of_opened < number_of_tags:
        curr_stack.append("<div>")
        generateDivTags_helper(resulting_sequence, curr_stack, number_of_tags, number_of_opened + 1)
        curr_stack.pop()
    if number_of_opened * 2 > len(curr_stack):
        curr_stack.append("</div>")
        generateDivTags_helper(resulting_sequence, curr_stack, number_of_tags, number_of_opened)
        curr_stack.pop()


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = 3
        expected = [
            "<div><div><div></div></div></div>",
            "<div><div></div><div></div></div>",
            "<div><div></div></div><div></div>",
            "<div></div><div><div></div></div>",
            "<div></div><div></div><div></div>",
        ]
        actual = generateDivTags(input)
        self.assertEqual(actual, expected)

    def test_case_2(self):
        input = 2
        expected = [
            "<div><div></div></div>",
            "<div></div><div></div>"
        ]
        actual = generateDivTags(input)
        self.assertEqual(actual, expected)
