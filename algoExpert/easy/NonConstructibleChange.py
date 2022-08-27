def non_constructible_change(coins):
    coins.sort()
    change_sum = 0
    for coin in coins:
        if coin > change_sum + 1:
            break
        change_sum += coin
    return change_sum + 1

    # complexity: O(n * lon(n))
    # space complexity: O(1)


if __name__ == '__main__':
    # 1, 1, 2, 3, 5, 7, 22
    assert non_constructible_change([5, 7, 1, 1, 2, 3, 22]) == 20
    assert non_constructible_change([1, 2, 5]) == 4
    assert non_constructible_change([7, 1, 2, 3, 22]) == 14
    assert non_constructible_change([]) == 1
    assert non_constructible_change([7]) == 1
    assert non_constructible_change([1, 1]) == 3


