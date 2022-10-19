# Solution 1.2
# O(2*n) time | O(n/2) space
# char_space
# space_char
def reverseWordsInString_1(string):
    resulting_list = []
    first_index = 0
    for i in range(0, len(string) - 1):
        if string[i] == " " and string[i + 1] != " " or string[i] != " " and string[i + 1] == " ":
            resulting_list.append(string[first_index:i + 1])
            first_index = i + 1
    resulting_list.append(string[first_index:len(string)])
    return "".join([resulting_list[i] for i in range(len(resulting_list) - 1, -1, -1)])


# Solution 1
# O(n) time | O(n/2) space
def reverseWordsInString_(string):
    resulting_list = []
    last_index = len(string) - 1
    for i in range(len(string) - 1, 0, -1):
        if string[i] == " " and string[i - 1] != " " or string[i] != " " and string[i - 1] == " ":
            resulting_list.append(string[i:last_index + 1])
            last_index = i - 1
    resulting_list.append(string[0:last_index + 1])
    return "".join(resulting_list)


# Solution 2
# O(n) time | O(n) space
def reverseWordsInString(string):
    reversed_string = [string[len(string) - 1 - i] for i in range(len(string))]
    start_index = 0
    for i in range(len(reversed_string)):
        if reversed_string[i] == " ":
            reverse_substr_inplace(reversed_string, start_index, i - 1)
            start_index = i + 1
    reverse_substr_inplace(reversed_string, start_index, len(reversed_string) - 1)
    return "".join(reversed_string)


def reverse_substr_inplace(string, start_index, end_index):
    middle = start_index + (end_index - start_index) // 2
    while end_index > middle:
        string[start_index], string[end_index] = string[end_index], string[start_index]
        start_index += 1
        end_index -= 1


if __name__ == '__main__':
    assert reverseWordsInString("AlgoExpert is the best!") == "best! the is AlgoExpert"
    assert reverseWordsInString("") == ""
    assert reverseWordsInString(" b") == "b "
    assert reverseWordsInString("b") == "b"
    assert reverseWordsInString("    ") == "    "
    assert reverseWordsInString(" a    ") == "    a "
    assert reverseWordsInString("a    ") == "    a"
    assert reverseWordsInString("    b") == "b    "
    assert reverseWordsInString("abc de  g ") == " g  de abc"
    assert reverseWordsInString(" abc de  g ") == " g  de abc "
    assert reverseWordsInString("abc de g") == "g de abc"
