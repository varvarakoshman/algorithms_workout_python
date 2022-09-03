# Solution 1 (a naive approach) - O(2^n) complexity | O(n) space
def get_nth_fib_1(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    return get_nth_fib_1(n - 1) + get_nth_fib_1(n - 2)


# Solution 2 (an improvement of Solution 1 (with cache)) - O(n) complexity | O(n) space
def get_nth_fib_2(n, cache=None):
    if cache is None:
        cache = {1: 0, 2: 1}
    if n not in cache.keys():
        cache[n] = get_nth_fib_2(n - 1, cache) + get_nth_fib_2(n - 2, cache)
    return cache[n]


# Solution 3 (an optimal one) - O(n) complexity | O(1) space
def get_nth_fib(n):
    last_pair = [0, 1]
    for i in range(3, n + 1):
        prev_sum = last_pair[0] + last_pair[1]
        last_pair[0] = last_pair[1]
        last_pair[1] = prev_sum
    return last_pair[1] if n > 1 else last_pair[0]


if __name__ == '__main__':
    assert get_nth_fib(2) == 1
    assert get_nth_fib(3) == 1
    assert get_nth_fib(5) == 3
    assert get_nth_fib(6) == 5
    assert get_nth_fib(8) == 13
