# O(n*logn) time | O(n) space
def mergeOverlappingIntervals(intervals):
    sorted_intervals = sorted(intervals)
    curr_interval = sorted_intervals[0]
    result = [curr_interval]

    for i in range(1, len(sorted_intervals)):
        new_interval = sorted_intervals[i]
        _, curr_interval_end = curr_interval
        new_interval_start, new_interval_end = new_interval

        if new_interval_start <= curr_interval_end:
            curr_interval[1] = max(new_interval_end, curr_interval_end)
        else:
            curr_interval = new_interval
            result.append(curr_interval)

    return result


if __name__ == '__main__':
    # every new interval (if overlaps) is either nested in a previous one or extends it
    assert mergeOverlappingIntervals([[1, 2], [3, 5], [4, 7], [6, 8], [9, 10]]) == [[1, 2], [3, 8], [9, 10]]
    assert mergeOverlappingIntervals([[1, 6], [6, 7]]) == [[1, 7]]
    assert mergeOverlappingIntervals([[1, 6], [2, 5]]) == [[1, 6]]
    assert mergeOverlappingIntervals([[1, 2], [3, 8], [9, 15]]) == [[1, 2], [3, 8], [9, 15]]
    assert mergeOverlappingIntervals([[1, 2]]) == [[1, 2]]
    assert mergeOverlappingIntervals([[1, 2], [2, 5], [4, 7], [6, 8], [9, 10]]) == [[1, 8], [9, 10]]
    assert mergeOverlappingIntervals([[1, 2], [3, 5], [6, 8], [7, 10]]) == [[1, 2], [3, 5], [6, 10]]
    assert mergeOverlappingIntervals([[1, 2], [1, 3], [1, 5]]) == [[1, 5]]
    assert mergeOverlappingIntervals([[-20, 30], [1, 22]]) == [[-20, 30]]
