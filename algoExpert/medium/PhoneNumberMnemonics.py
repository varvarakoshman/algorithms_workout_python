# Solution 1 - iterative approach
# O(n * 4^n) time | O(n * 4^n) space
# 4^n - # of resulting combinations
def phoneNumberMnemonics_1(phoneNumber):
    first_digit = int(phoneNumber[0])
    result = [[letter] for letter in DIGIT_MAPPING[first_digit]]
    for i in range(1, len(phoneNumber)):
        digit_num = int(phoneNumber[i])
        curr_mapping = DIGIT_MAPPING[digit_num]
        new_result = []
        for resulting_entry in result:
            for letter in curr_mapping:
                new_entry = [resulting_entry[count] for count in range(i)]
                new_entry.append(letter)
                new_result.append(new_entry)
        result = new_result
    joined_strings = [''.join(result_entry) for result_entry in result]
    return joined_strings


# Solution 2 - recursive approach
# same time & space complexity
def phoneNumberMnemonics(phoneNumber):
    mnemonics_found = []
    get_mnemonics_helper(0, phoneNumber, [''] * len(phoneNumber), mnemonics_found)
    return mnemonics_found


def get_mnemonics_helper(index, phoneNumber, current, mnemonics_found):
    if index == len(current):
        mnemonics_found.append(''.join(current))
    else:
        curr_digit = int(phoneNumber[index])
        for letter in DIGIT_MAPPING[curr_digit]:
            current[index] = letter
            get_mnemonics_helper(index + 1, phoneNumber, current, mnemonics_found)


DIGIT_MAPPING = {
    0: ['0'],
    1: ['1'],
    2: ['a', 'b', 'c'],
    3: ['d', 'e', 'f'],
    4: ['g', 'h', 'i'],
    5: ['j', 'k', 'l'],
    6: ['m', 'n', 'o'],
    7: ['p', 'q', 'r', 's'],
    8: ['t', 'u', 'v'],
    9: ['w', 'x', 'y', 'z']
}

if __name__ == '__main__':
    assert phoneNumberMnemonics("1905") == ["1w0j", "1w0k", "1w0l", "1x0j", "1x0k", "1x0l", "1y0j",
                                            "1y0k", "1y0l", "1z0j", "1z0k", "1z0l"]
