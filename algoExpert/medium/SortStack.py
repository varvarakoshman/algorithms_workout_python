# O(n^2) time | O(n) space - optimal in terms of requirements
def sort_stack(stack):
    top_elem = None
    if len(stack) > 1:
        top_elem = stack.pop()
        stack = sort_stack(stack)
    if top_elem is not None:
        insert_in_sorted_stack(stack, top_elem)
    return stack


def insert_in_sorted_stack(stack, elem):
    if len(stack) == 0 or elem >= stack[-1]:
        stack.append(elem)
    else:
        top_elem = stack.pop()
        insert_in_sorted_stack(stack, elem)
        stack.append(top_elem)


if __name__ == '__main__':
    assert sort_stack([-5, 2, -2, 4, 3, 1]) == [-5, -2, 1, 2, 3, 4]
    assert sort_stack([]) == []
    assert sort_stack([3]) == [3]
    assert sort_stack([2, 1]) == [1, 2]
    assert sort_stack([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert sort_stack([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
