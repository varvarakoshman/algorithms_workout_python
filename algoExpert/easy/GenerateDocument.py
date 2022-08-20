def generate_document(characters, document):
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
    assert generate_document("Bste!hetsi ogEAxpelrt x ", "AlgoExpert is the Best!") == True
    assert generate_document("A", "a") == False
    assert generate_document("a", "a") == True
    assert generate_document("a hsgalhsa sanbjksbdkjba kjx", "") == True
    assert generate_document(" ", "hello") == False
    assert generate_document("     ", "     ") == True
    assert generate_document("aheaollabbhb", "hello") == True
    assert generate_document("aheaolabbhb", "hello") == False
    assert generate_document("estssa", "testing") == False
    assert generate_document("Bste!hetsi ogEAxpert", "AlgoExpert is the Best!") == False
    assert generate_document("helloworld ", "hello wOrld") == False
    assert generate_document("helloworldO", "hello wOrld") == False
    assert generate_document("&*&you^a%^&8766 _=-09     docanCMakemthisdocument", "Can you make this document &") == True
    assert generate_document("abcabcabcacbcdaabc", "bacaccadac") == True
