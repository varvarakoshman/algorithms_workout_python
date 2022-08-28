def tandem_bicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    redShirtSpeeds.sort(reverse=fastest)
    blueShirtSpeeds.sort()
    return get_speed_sum(redShirtSpeeds, blueShirtSpeeds)


def get_speed_sum(redShirtSpeeds, blueShirtSpeeds):
    speed_sum = 0
    for i in range(len(redShirtSpeeds)):
        speed_sum += max(redShirtSpeeds[i], blueShirtSpeeds[i])
    return speed_sum

    # complexity: O(n * log(n))
    # space complexity: O(1)


if __name__ == '__main__':
    assert tandem_bicycle([5, 5, 3, 9, 2], [3, 6, 7, 2, 1], True) == 32
    assert tandem_bicycle([1, 4], [5, 3], True) == 9
    assert tandem_bicycle([4, 4, 4], [4, 4, 4], True) == 12
    assert tandem_bicycle([4, 4, 4], [4, 4, 4], False) == 12
    assert tandem_bicycle([1, 4], [5, 3], False) == 8
    assert tandem_bicycle([5, 5, 3, 9, 2], [3, 6, 7, 2, 1], False) == 25
