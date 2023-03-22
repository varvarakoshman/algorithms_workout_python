# Solution 1 - O(n^2) time | O(n) space - naive approach
# for each element in an input array check next elements to find 1st greater

# Solution 2 - O(n*logn) time | O(2n)=O(n) space
# storing a sorted version of an input array

# Solution 3 - optimal - O(n) time | O(n) space
def nextGreaterElement(array):
    result = [-1] * len(array)
    stack = [0]
    for i in range(1, 2 * len(array)):
        if len(stack) == 0:
            break
        curr_index = i % len(array)
        while len(stack) > 0 and array[curr_index] > array[stack[-1]]:
            result[stack[-1]] = array[curr_index]
            stack.pop()
        stack.append(curr_index)
    return result


if __name__ == '__main__':
    assert nextGreaterElement([2, 5, -3, -4, 6, 7, 2]) == [5, 6, 6, 6, 7, -1, 5]
    assert nextGreaterElement([0, 0, 5, 0, 0, 3, 0, 0]) == [5, 5, -1, 3, 3, 5, 5, 5]
    assert nextGreaterElement([7, 6, 5, 4, 3]) == [-1, 7, 7, 7, 7]
    assert nextGreaterElement([1, 2]) == [2, -1]
    assert nextGreaterElement([2]) == [-1]
    assert nextGreaterElement([]) == []

#
# [2, 5, -3, -4, 6, 7, 2]
# [-4, -3, 2, 2, 5, 6, 7]
#
# {
#     2: 0,
#     -4: 3,
#     2: 6,
#     6: 4,
#     5: 1,
#     -3: 2,
#     7: 5
# }