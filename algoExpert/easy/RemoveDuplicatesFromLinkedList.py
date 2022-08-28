class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __eq__(self, other):
        if isinstance(other, LinkedList):
            return self.value == other.value and self.next == other.next
        return False


# Solution 1
def remove_duplicates_from_linkedlist_2(linkedlist):
    prev = LinkedList(None)
    head = linkedlist
    while head is not None:
        if head.value == prev.value:
            prev.next = head.next
        else:
            prev = head
        head = head.next
    return linkedlist

    # complexity: O(n)
    # space complexity: O(1)


# Solution 2 - jump over all duplicate values at once (a lower number of a pointer's changes)
# 1 -> 1 -> 3 -> 4 -> 4 -> 4 -> 5 -> 6 -> 6
def remove_duplicates_from_linkedlist(linkedlist):
    curr_node = linkedlist
    while curr_node is not None:
        next_distinct = curr_node.next
        while next_distinct is not None and next_distinct.value == curr_node.value:
            next_distinct = next_distinct.next
        curr_node.next = next_distinct
        curr_node = next_distinct
    return linkedlist

    # complexity: O(n)
    # space complexity: O(1)


def get_input_1_data():
    node1 = LinkedList(1)
    node2 = LinkedList(1)
    node1.next = node2
    node3 = LinkedList(3)
    node2.next = node3
    node4 = LinkedList(4)
    node3.next = node4
    node5 = LinkedList(4)
    node4.next = node5
    node6 = LinkedList(4)
    node5.next = node6
    node7 = LinkedList(5)
    node6.next = node7
    node8 = LinkedList(6)
    node7.next = node8
    node9 = LinkedList(6)
    node8.next = node9
    return node1


def get_output_1_data():
    node1 = LinkedList(1)
    node2 = LinkedList(3)
    node1.next = node2
    node3 = LinkedList(4)
    node2.next = node3
    node4 = LinkedList(5)
    node3.next = node4
    node5 = LinkedList(6)
    node4.next = node5
    return node1


def get_input_2_data():
    node1 = LinkedList(1)
    prev = node1
    for _ in range(3):
        new_node = LinkedList(1)
        prev.next = new_node
        prev = new_node
    return node1


if __name__ == '__main__':
    # 1 -> 1 -> 3 -> 4 -> 4 -> 4 -> 5 -> 6 -> 6
    # 1 -> 3 -> 4 -> 5 -> 6
    assert remove_duplicates_from_linkedlist(get_input_1_data()) == get_output_1_data()
    # 1
    # 1
    assert remove_duplicates_from_linkedlist(LinkedList(1)) == LinkedList(1)
    # 1 -> 1 -> 1 -> 1
    # 1
    assert remove_duplicates_from_linkedlist(get_input_2_data()) == LinkedList(1)
    # None
    # None
    assert remove_duplicates_from_linkedlist(None) is None



