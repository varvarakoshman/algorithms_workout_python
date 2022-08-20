def generateDocument(characters, document):
    chars_frequencies = generate_frequencies(characters)
    doc_frequencies = generate_frequencies(document)
    return is_contained(document, chars_frequencies, doc_frequencies)


def generate_frequencies(string):
    frequencies = {}
    for char in string:
        frequencies[char] = frequencies.get(char, 0) + 1
    return frequencies


def is_contained(document, chars_frequencies, doc_frequencies):
    is_contained = True
    for char in document:
        if char not in chars_frequencies.keys() or chars_frequencies[char] < doc_frequencies[char]:
            is_contained = False
    return is_contained


if __name__ == '__main__':
    assert generateDocument("Bste!hetsi ogEAxpelrt x ", "AlgoExpert is the Best!") == True
    assert generateDocument("A", "a") == False
    assert generateDocument("a", "a") == True
    assert generateDocument("a hsgalhsa sanbjksbdkjba kjx", "") == True
    assert generateDocument(" ", "hello") == False
    assert generateDocument("     ", "     ") == True
    assert generateDocument("aheaollabbhb", "hello") == True
    assert generateDocument("aheaolabbhb", "hello") == False
    assert generateDocument("estssa", "testing") == False
    assert generateDocument("Bste!hetsi ogEAxpert", "AlgoExpert is the Best!") == False
    assert generateDocument("helloworld ", "hello wOrld") == False
    assert generateDocument("helloworldO", "hello wOrld") == False
    assert generateDocument("&*&you^a%^&8766 _=-09     docanCMakemthisdocument", "Can you make this document &") == True
    assert generateDocument("abcabcabcacbcdaabc", "bacaccadac") == True
