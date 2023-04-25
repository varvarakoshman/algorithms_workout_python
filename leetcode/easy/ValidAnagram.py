# O(n) time | O(n) space
def isAnagram(string_one, string_two):
    letter_frequencies_one = get_letter_frequencies(string_one)
    letter_frequencies_two = get_letter_frequencies(string_two)
    return letter_frequencies_one == letter_frequencies_two


def get_letter_frequencies(string):
    frequencies = {}
    for letter in string:
        if letter in frequencies:
            frequencies[letter] += 1
        else:
            frequencies[letter] = 0
    return frequencies


if __name__ == '__main__':
    assert isAnagram("anagram", "nagaram") is True
    assert isAnagram("rat", "car") is False
    assert isAnagram("a", "a") is True
    assert isAnagram("aba", "baa") is True
    assert isAnagram("abac", "baa") is False
    assert isAnagram("", "") is True
