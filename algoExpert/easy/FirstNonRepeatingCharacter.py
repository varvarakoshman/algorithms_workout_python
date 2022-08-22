def first_non_repeating_character(string):
    char_count = {}
    for index, char in enumerate(string):
        char_count[char] = char_count.get(char, 0) + 1
    for index, char in enumerate(string):
        if char_count[char] == 1:
            return index
    return -1

    # complexity: O(n)
    # space complexity: O(1)


if __name__ == '__main__':
    assert first_non_repeating_character("abcdcaf") == 1
    assert first_non_repeating_character("a") == 0
    assert first_non_repeating_character("ab") == 0
    assert first_non_repeating_character("ababac") == 5
    assert first_non_repeating_character("") == -1
    assert first_non_repeating_character("aabbccddjktt") == 8