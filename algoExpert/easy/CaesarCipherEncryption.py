# Solution 1 (without Unicode built-in functions)
alphabet = list("abcdefghijklmnopqrstuvwxyz")


def caesar_cipher_encryptor_1(string, key):
    key = key % len(alphabet)
    shifted_str = []
    for char in string:
        shifted_str.append(get_shifted_char_1(char, key))
    return "".join(shifted_str)


def get_shifted_char_1(char, key):
    new_index = alphabet.index(char) + key
    if new_index > len(alphabet) - 1:
        return alphabet[new_index - len(alphabet)]
    else:
        return alphabet[new_index]

    # complexity: O(n)
    # space complexity: O(n)


# Solution 2 (has same time & space complexities, but utilizes built-in functions)
# Unicode:
# z => 122
# a => 97
def caesar_cipher_encryptor(string, key):
    key = key % 26
    shifted_str = []
    for char in string:
        shifted_str.append(get_shifted_char(char, key))
    return "".join(shifted_str)


def get_shifted_char(char, key):
    new_index = ord(char) + key
    if new_index > 122:
        return chr(96 + new_index % 122)
    else:
        return chr(new_index)

    # complexity: O(n)
    # space complexity: O(n)


if __name__ == '__main__':
    assert caesar_cipher_encryptor("xyz", 2) == "zab"
    assert caesar_cipher_encryptor("xyz", 5) == "cde"
    assert caesar_cipher_encryptor("abc", 3) == "def"
    assert caesar_cipher_encryptor("abc", 0) == "abc"
    assert caesar_cipher_encryptor("abc", 26) == "abc"
    assert caesar_cipher_encryptor("abc", 52) == "abc"
    assert caesar_cipher_encryptor("abc", 57) == "fgh"
    assert caesar_cipher_encryptor("xyz", 25) == "wxy"
