# O(n) time | O(n) space
def sunset_views(buildings, direction):
    if direction == "WEST":
        direction_range = range(len(buildings))
    else:
        direction_range = reversed(range(len(buildings)))
    result = []
    local_max = 0
    for i in direction_range:
        curr_height = buildings[i]
        if curr_height > local_max:
            result.append(i)
            local_max = curr_height
    if direction == "EAST":
        result.reverse()
    return result


if __name__ == '__main__':
    assert sunset_views([3, 5, 4, 4, 3, 1, 3, 2], "EAST") == [1, 3, 6, 7]
    assert sunset_views([3, 5, 4, 4, 3, 1, 3, 2], "WEST") == [0, 1]
    assert sunset_views([1, 2, 3, 4, 5], "WEST") == [0, 1, 2, 3, 4]
    assert sunset_views([1, 2, 3, 4, 5], "EAST") == [4]
    assert sunset_views([1], "EAST") == [0]
    assert sunset_views([], "WEST") == []
