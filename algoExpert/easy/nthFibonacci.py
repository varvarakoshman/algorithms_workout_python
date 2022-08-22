def get_nth_fib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    return get_nth_fib(n - 1) + get_nth_fib(n - 2)

    # complexity: O(n)
    # space complexity: O(1)


if __name__ == '__main__':
    assert get_nth_fib(2) == 1
    assert get_nth_fib(3) == 1
    assert get_nth_fib(5) == 3
    assert get_nth_fib(6) == 5
    assert get_nth_fib(8) == 13
