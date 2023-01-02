# Solution 1
# O(n^2) time | O(n) space
def threeNumberSum_1(array, targetSum):
    array.sort()
    result = []
    for i in range(1, len(array) - 1):
        central = array[i]
        right_pointer = i + 1
        left_pointer = i - 1
        while left_pointer >= 0 and right_pointer < len(array):
            curr_sum = central + array[left_pointer] + array[right_pointer]
            if curr_sum == targetSum:
                result.append([array[left_pointer], central, array[right_pointer]])
                right_pointer += 1
                left_pointer -= 1
            elif curr_sum > targetSum:
                left_pointer -= 1
            else:
                right_pointer += 1
    result.sort()
    return result

# Solution 1.2
# same solution, but different manipulations with pointers
# O(n^2) time | O(n) space
def threeNumberSum(array, targetSum):
    array.sort()
    result = []
    for i in range(len(array) - 2):
        currNum = array[i]
        left_pointer = i + 1
        right_pointer = len(array) - 1
        while left_pointer < right_pointer:
            curr_sum = currNum + array[right_pointer] + array[left_pointer]
            if curr_sum == targetSum:
                result.append([currNum, array[left_pointer], array[right_pointer]])
                left_pointer += 1
                right_pointer -= 1
            elif curr_sum > targetSum:
                right_pointer -= 1
            else:
                left_pointer += 1
    result.sort()
    return result



if __name__ == '__main__':
    assert threeNumberSum([12, 3, 1, 2, -6, 5, -8, 6], 0) == [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]
    assert threeNumberSum([3, 4, 2, 1, 0], 5) == [[0, 1, 4], [0, 2, 3]]
    assert threeNumberSum([12, 3, 1, 2, -6, 5, -8, 6], 255) == []
    assert threeNumberSum([1, 2, 3], 5) == []
    assert threeNumberSum([3, 1, 2], 6) == [[1, 2, 3]]
    assert threeNumberSum([3, 1, 2, -6], 6) == [[1, 2, 3]]
    assert threeNumberSum([1, 2, 3, 4, 5, 6], 12) == [[1, 5, 6], [2, 4, 6], [3, 4, 5]]
