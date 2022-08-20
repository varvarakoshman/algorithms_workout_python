alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


def caesar_cipher_encryptor(string, key):
    key = key % len(alphabet)
    shifted_str = ""
    for char in string:
        shifted_str += get_shifted_char(char, key)
    return shifted_str


def get_shifted_char(char, key):
    new_index = alphabet.index(char) + key
    if new_index > len(alphabet) - 1:
        return alphabet[new_index - len(alphabet)]
    else:
        return alphabet[new_index]


if __name__ == '__main__':
    assert caesar_cipher_encryptor("xyz", 2) == "zab"