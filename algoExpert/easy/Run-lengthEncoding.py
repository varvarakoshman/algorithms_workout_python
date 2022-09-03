def run_length_encoding(string):
    curr_count = 1
    output = []
    for i in range(1, len(string)):
        current_char = string[i]
        previous = string[i - 1]
        if current_char != previous or curr_count == 9:
            output.append(str(curr_count))
            output.append(str(previous))
            curr_count = 0
        curr_count += 1
    output.append(str(curr_count))
    output.append(str(string[-1]))
    return ''.join(output)

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