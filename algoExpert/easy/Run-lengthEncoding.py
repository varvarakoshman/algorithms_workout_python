def run_length_encoding(string):
    index_char_mapping = get_chars_mapping(string)
    output = str()
    indices = list(index_char_mapping.keys())
    for i in range(1, len(indices)):
        cur_len = indices[i] - indices[i - 1]
        char = index_char_mapping[indices[i - 1]]
        output += get_new_seq(char, cur_len)
    last_char_index = indices[-1]
    last_char = index_char_mapping[last_char_index]
    output += get_new_seq(last_char, len(string) - last_char_index)
    return output


def get_chars_mapping(string):
    index_char_mapping = {}
    previous = ""
    for i in range(len(string)):
        if string[i] != previous:
            previous = string[i]
            index_char_mapping[i] = previous
    return index_char_mapping


def get_new_seq(char, cur_len):
    if cur_len <= 9:
        return str(cur_len) + char
    else:
        full_seq_num = cur_len // 9
        remaining_num = cur_len % 9
        single_full_seq = "9" + char
        return single_full_seq * full_seq_num + str(remaining_num) + char

    # complexity: O(n)
    # space complexity: O(n)


if __name__ == '__main__':
    assert run_length_encoding("AAA") == "3A"
    assert run_length_encoding("AAAB") == "3A1B"
    assert run_length_encoding("AAAAAAAAAAAA") == "9A3A"
    assert run_length_encoding("AAAAAAAAAAAAABBCCCCDD") == "9A4A2B4C2D"
    assert run_length_encoding("A") == "1A"
    assert run_length_encoding("AAAAAAAAA") == "9A"

    # 0: A
    #
    # 0: A
    # 3: B