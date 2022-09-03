# Solution 1 (brute force)
# characters: "Bste!hetsi ogEAxpelrt x " (n)
# document:   "AlgoExpert is the Best!"  (m)
# complexity: O(m * (m + n))
# space complexity: O(1)
# drawback: # Ex: "AAAAAAAAAAA" => "AAAAAAA" - each letter gets calculated on each iteration over again
def generate_document_1(characters, document):
    for char in document:
        count_doc = get_char_сount_1(document, char)
        count_chars = get_char_сount_1(characters, char)
        if count_chars < count_doc:
            return False
    return True


def get_char_сount_1(char_seq, target_char):
    count = 0
    for char in char_seq:
        if char == target_char:
            count += 1
    return count


# Solution 2 (almost identical to Solution 1) (an improvement of a brute force approach)
# "Bste!hetsi ogEAxpelrt x " => "AlgoExpert is the Best!"
# save already calculated frequencies in a cache
# complexity: O(c * (m + n)), c - # of unique characters in a document
# space complexity: O(c)
def generate_document_2(characters, document):
    counted_cache = {}
    for char in document:
        if char in counted_cache.keys():
            continue
        count_doc = get_char_сount(document, char)
        count_chars = get_char_сount(characters, char)
        if count_chars < count_doc:
            return False
        counted_cache[char] = count_doc
    return True


def get_char_сount(char_seq, target_char):
    count = 0
    for char in char_seq:
        if char == target_char:
            count += 1
    return count


# Solution 3 (an optimal one) (store frequencies in a hashmap - calculate once & store)
# characters: "Bste!hetsi ogEAxpelrt x " (n)
# document:   "AlgoExpert is the Best!"  (m)
# complexity: O(n + m)
# space complexity: O(c)
def generate_document(characters, document):
    chars_frequencies = generate_frequencies(characters)
    for char in document:
        if char not in chars_frequencies.keys() or chars_frequencies[char] == 0:
            return False
        chars_frequencies[char] -= 1
    return True


def generate_frequencies(string):
    frequencies = {}
    for char in string:
        frequencies[char] = frequencies.get(char, 0) + 1
    return frequencies


# My initial solution - slightly worse than the optimal in terms of space:
# complexity: O(n + m) | space: O(c1 + c2)

# def generateDocument(characters, document):
#     chars_frequencies = generate_frequencies(characters)
#     doc_frequencies = generate_frequencies(document)
#     return is_contained(document, chars_frequencies, doc_frequencies)
#
#
# def generate_frequencies(string):
#     frequencies = {}
#     for char in string:
#         frequencies[char] = frequencies.get(char, 0) + 1
#     return frequencies
#
#
# def is_contained(document, chars_frequencies, doc_frequencies):
#     is_contained = True
#     for char in document:
#         if char not in chars_frequencies.keys() or chars_frequencies[char] < doc_frequencies[char]:
#             is_contained = False
#     return is_contained


if __name__ == '__main__':
    assert generate_document("Bste!hetsi ogEAxpelrt x ", "AlgoExpert is the Best!") is True
    assert generate_document("A", "a") is False
    assert generate_document("a", "a") is True
    assert generate_document("a hsgalhsa sanbjksbdkjba kjx", "") is True
    assert generate_document(" ", "hello") is False
    assert generate_document("     ", "     ") is True
    assert generate_document("aheaollabbhb", "hello") is True
    assert generate_document("aheaolabbhb", "hello") is False
    assert generate_document("estssa", "testing") is False
    assert generate_document("Bste!hetsi ogEAxpert", "AlgoExpert is the Best!") is False
    assert generate_document("helloworld ", "hello wOrld") is False
    assert generate_document("helloworldO", "hello wOrld") is False
    assert generate_document("&*&you^a%^&8766 _=-09     docanCMakemthisdocument", "Can you make this document &") is True
    assert generate_document("abcabcabcacbcdaabc", "bacaccadac") is True
