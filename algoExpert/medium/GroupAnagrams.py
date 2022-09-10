# Solution 1 (optimal): O(w * nlog(n)) time | O(wn) space,
# w - number of words, n - length of the longest word
def group_anagrams(words):
    word_forms = {}
    for word in words:
        sorted_word = ''.join(sorted(word))
        if sorted_word not in word_forms.keys():
            word_forms[sorted_word] = [word]
        else:
            word_forms[sorted_word].append(word)
    return list(word_forms.values())


# Solution 2 (alternative: same asymptotic, but harder to implement): O(w * nlog(n)) time | O(wn) space,
# w - number of words, n - length of the longest word
def group_anagram_2(words):
    if len(words) == 0:
        return []
    sorted_words = [''.join(sorted(word)) for word in words]
    indices = [index for index in range(len(words))]
    sorted_indices = sorted(indices, key=lambda x: sorted_words[x])
    grouped_anagrams = []
    current_group = []
    previous = sorted_words[sorted_indices[0]]
    for index in sorted_indices:
        word = words[index]
        sorted_word = sorted_words[index]
        if sorted_word == previous:
            current_group.append(word)
        else:
            previous = sorted_word
            grouped_anagrams.append(current_group)
            current_group = [word]
    grouped_anagrams.append(current_group)
    return grouped_anagrams

# Ex:
# words = ["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]
# sorted_words = ["oy", "act", "flop", "act", "act", "oy", "flop"]
# indices = [0, 1, 2, 3, 4, 5, 6]
# sorted_indices = [1, 3, 4, 2, 6, 0, 5]


if __name__ == '__main__':
    assert group_anagrams(["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]) == \
           [
               ["yo", "oy"],
               ["act", "tac", "cat"],
               ["flop", "olfp"],
               ["foo"]
           ]
    assert group_anagrams(["yyo", "yo"]) == [["yyo"], ["yo"]]
    assert group_anagrams(["yo", "oy", "zn"]) == [["yo", "oy"], ["zn"]]
    assert group_anagrams(["abc", "def", "xyz"]) == [["abc"], ["def"], ["xyz"]]
    assert group_anagrams(["aaaa", "aaaa", "aaaa"]) == [["aaaa", "aaaa", "aaaa"]]
    assert group_anagrams(["", "", ""]) == [["", "", ""]]
    assert group_anagrams([]) == []
