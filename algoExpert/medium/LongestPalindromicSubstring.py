# Solution - O(n^2) time | O(n) space (my initial one)
def longest_palindromic_substring(string):
    possible_borders = []
    for i in range(1, len(string)):
        if string[i] == string[i - 1]:
            possible_borders.append([i - 1, i])
        if i >= 2 and string[i] == string[i - 2]:
            possible_borders.append([i - 2, i])
    max_borders = [0, 1]
    for borders_pair in possible_borders:
        curr_borders = get_palindrome_borders(string, borders_pair)
        max_borders = max(max_borders, curr_borders, key=lambda x: x[1] - x[0])
    return string[max_borders[0]: max_borders[1]]


def get_palindrome_borders(string, borders_pair):
    step = 1
    while borders_pair[0] - step >= 0 and borders_pair[1] + step < len(string) and \
            string[borders_pair[0] - step] == string[borders_pair[1] + step]:
        step += 1
    step -= 1
    return [borders_pair[0] - step, borders_pair[1] + step + 1]


# Slightly modified (same complexity) solution - no extra list
def longest_palindromic_substring_2(string):
    max_borders = [0, 1]
    for i in range(1, len(string)):
        odd_borders = get_palindrome_borders_2(string, i - 1, i + 1)
        even_borders = get_palindrome_borders_2(string, i - 1, i)
        max_borders = max(max_borders, odd_borders, even_borders, key=lambda x: x[1] - x[0])
    return string[max_borders[0]: max_borders[1]]


def get_palindrome_borders_2(string, left_idx, right_idx):
    while left_idx >= 0 and right_idx < len(string):
        if string[left_idx] != string[right_idx]:
            break
        right_idx += 1
        left_idx -= 1
    return [left_idx + 1, right_idx]


if __name__ == '__main__':
    assert longest_palindromic_substring("abaxyzzyxf") == "xyzzyx"
    assert longest_palindromic_substring("aaaaa") == "aaaaa"
    assert longest_palindromic_substring("abcddcbaabccba") == "abcddcba"
    assert longest_palindromic_substring("abccbaabcddcba") == "abcddcba"
    assert longest_palindromic_substring("abccbaabcdcba") == "abcdcba"
    assert longest_palindromic_substring("abcdcbaabccba") == "abcdcba"
    assert longest_palindromic_substring("a") == "a"
    assert longest_palindromic_substring("") == ""

# dabccbakfabcdcba
#  ______  _______
#  len=6    len=7
