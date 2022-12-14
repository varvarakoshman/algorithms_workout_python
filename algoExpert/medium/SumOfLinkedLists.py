# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __eq__(self, other):
        if isinstance(other, LinkedList):
            return self.value == other.value and self.next == other.next
        return False


# O(max(n, m)) time | O(max(n, m)) space
def sumOfLinkedLists(linkedListOne, linkedListTwo):
    curr_node = LinkedList(0)
    result_head = curr_node
    remainder = 0
    while linkedListOne is not None or linkedListTwo is not None:
        curr_sum = remainder + get_sum(linkedListOne, linkedListTwo)
        new_digit = curr_sum % 10
        remainder = curr_sum // 10

        new_node = LinkedList(new_digit)
        curr_node.next = new_node
        curr_node = new_node

        if linkedListOne is not None:
            linkedListOne = linkedListOne.next
        if linkedListTwo is not None:
            linkedListTwo = linkedListTwo.next
    if remainder == 1:
        curr_node.next = LinkedList(1)
    return result_head.next


def get_sum(linkedListOne, linkedListTwo):
    curr_sum = 0
    if linkedListOne is not None:
        curr_sum += linkedListOne.value
    if linkedListTwo is not None:
        curr_sum += linkedListTwo.value
    return curr_sum


def get_input_1_data():
    node1 = LinkedList(2)
    node2 = LinkedList(4)
    node1.next = node2
    node3 = LinkedList(7)
    node2.next = node3
    node4 = LinkedList(1)
    node3.next = node4
    return node1


def get_input_2_data():
    node1 = LinkedList(9)
    node2 = LinkedList(4)
    node1.next = node2
    node3 = LinkedList(5)
    node2.next = node3
    return node1


def get_output_1_data():
    node1 = LinkedList(1)
    node2 = LinkedList(9)
    node1.next = node2
    node3 = LinkedList(2)
    node2.next = node3
    node4 = LinkedList(2)
    node3.next = node4
    return node1


if __name__ == '__main__':
    # 2 -> 4 -> 7 -> 1
    # 9 -> 4 -> 5
    # 1 -> 9 -> 2 -> 2
    assert sumOfLinkedLists(get_input_1_data(), get_input_2_data()) == get_output_1_data()

