# input string length <= 12
# IP address - 4 positive integers [0-255]
# no leading 0s allowed

# O(1) time | O(1) space
def validIPAddresses(string):
    result = []
    for i in range(len(string) - 3):
        first_number = string[0:i + 1]
        if not is_valid_number(first_number):
            continue
        for j in range(i + 1, len(string) - 2):
            second_number = string[i + 1:j + 1]
            if not is_valid_number(second_number):
                continue
            for k in range(j + 1, len(string) - 1):
                third_number = string[j + 1:k + 1]
                forth_number = string[k + 1:len(string)]
                if not is_valid_number(third_number) or not is_valid_number(forth_number):
                    continue
                valid_ip = ".".join([first_number, second_number, third_number, forth_number])
                result.append(valid_ip)
    return result


def is_valid_number(str_number):
    number = int(str_number)
    return number >= 0 and number <= 255 and len(str(number)) == len(str_number)


if __name__ == '__main__':
    assert validIPAddresses("1921680") == ["1.9.216.80", "1.92.16.80", "1.92.168.0",
                                           "19.2.16.80", "19.2.168.0", "19.21.6.80", "19.21.68.0", "19.216.8.0",
                                           "192.1.6.80", "192.1.68.0", "192.16.8.0"]
    assert validIPAddresses("1234") == ["1.2.3.4"]
    assert validIPAddresses("") == []