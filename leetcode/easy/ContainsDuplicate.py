# O(n) time | O(n) space
def containsDuplicate(nums):
    already_seen = set()
    for num in nums:
        if num in already_seen:
            return True
        else:
            already_seen.add(num)
    return False


if __name__ == '__main__':
    assert containsDuplicate([1, 2, 3, 1]) is True
    assert containsDuplicate([1, 2, 3, 4]) is False
    assert containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) is True
    assert containsDuplicate([1]) is False
    assert containsDuplicate([]) is False
