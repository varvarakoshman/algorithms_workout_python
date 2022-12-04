# Solution 1
# O(n * l) time | O(n * l) space, n - # of words, l - length of the longest one
def minimumCharactersForWords(words):
    all_freq = {}
    for word in words:
        curr_freq = get_frequencies(word)
        extend_global_dict(all_freq, curr_freq)
    return [letter for letter, freq in all_freq.items() for _ in range(freq)]


def get_frequencies(word):
    frequencies = {}
    for char in word:
        if char not in frequencies:
            frequencies[char] = 1
        else:
            frequencies[char] += 1
    return frequencies


def extend_global_dict(all_freq, curr_freq):
    for char, freq in curr_freq.items():
        if char not in all_freq or all_freq[char] < freq:
            all_freq[char] = freq


if __name__ == '__main__':
    assert minimumCharactersForWords(["this", "that", "did", "deed", "them!", "a"]) == \
           ['t', 't', 'h', 'i', 's', 'a', 'd', 'd', 'e', 'e', 'm', '!']
    assert minimumCharactersForWords(["aaaaaa"]) == ['a', 'a', 'a', 'a', 'a', 'a']
    assert minimumCharactersForWords([]) == []
    assert minimumCharactersForWords(["aaaa", "aaa", "a"]) == ['a', 'a', 'a', 'a']
    assert minimumCharactersForWords(["abc", "defg", "h"]) == ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    assert minimumCharactersForWords(['123', '2345', '22', '44']) == ['1', '2', '2', '3', '4', '4', '5']
    assert minimumCharactersForWords(["../;", ";.", "!!", "/.;;"]) == ['.', '.', '/', ';', ';', '!', '!']
