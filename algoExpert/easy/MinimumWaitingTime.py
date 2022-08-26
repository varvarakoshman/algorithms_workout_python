def minimum_waiting_time(queries):
    queries.sort()
    total_time = 0

    for i in range(1, len(queries)):
        total_time += sum(queries[:i])
    return total_time

    # complexity: O(n * log(n))
    # space complexity: O(1)


if __name__ == '__main__':
    assert minimum_waiting_time([3, 2, 1, 2, 6]) == 17
    assert minimum_waiting_time([5, 1, 4]) == 6
    assert minimum_waiting_time([2, 1, 1, 1]) == 6
    assert minimum_waiting_time([1, 2, 4, 5, 2, 1]) == 23
    assert minimum_waiting_time([5]) == 0
    assert minimum_waiting_time([1, 2, 3, 4, 5]) == 20
    assert minimum_waiting_time([5, 4, 3, 2, 1]) == 20
