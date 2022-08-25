def class_photos(redShirtHeights, blueShirtHeights):
    redShirtHeights.sort()
    blueShirtHeights.sort()
    is_bigger = is_nested(redShirtHeights, blueShirtHeights)
    is_smaller = is_nested(blueShirtHeights, redShirtHeights)
    return is_bigger or is_smaller


def is_nested(lower_row, upper_row):
    for i in range(len(lower_row)):
        if lower_row[i] >= upper_row[i]:
            return False
    return True

    # complexity: O(n * log(n))
    # space complexity: O(1)


if __name__ == '__main__':
    assert class_photos([5, 8, 1, 3, 4], [6, 9, 2, 4, 5]) is True
    assert class_photos([1, 4], [5, 3]) is True
    assert class_photos([1, 4], [1, 4]) is False
    assert class_photos([1, 2, 3, 4, 5], [1, 6, 7, 8, 9]) is False
    assert class_photos([5, 5, 5], [6, 6, 6]) is True
