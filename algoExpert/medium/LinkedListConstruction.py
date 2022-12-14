# None <- 1 <-> 2 <-> 3 <-> 4 <-> 5 -> None
# This is an input class. Do not edit.
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


# Feel free to add new properties and methods to the class.
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # O(1) time | O(1) space
    def setHead(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            return
        self.insertBefore(self.head, node)

    # O(1) time | O(1) space
    def setTail(self, node):
        if self.tail is None:
            self.setHead(node)
            return
        self.insertAfter(self.tail, node)

    # None <-> (node)
    # (node) <-> None
    # None <- (node) -> None
    # O(1) time | O(1) space
    def insertBefore(self, node, nodeToInsert):
        if self.head == nodeToInsert and self.tail == nodeToInsert:
            return
        self.remove(nodeToInsert)
        nodeToInsert.prev = node.prev
        nodeToInsert.next = node
        if node.prev is None:
            self.head = nodeToInsert
        else:
            node.prev.next = nodeToInsert
        node.prev = nodeToInsert

    # (node) <-> ()
    # O(1) time | O(1) space
    def insertAfter(self, node, nodeToInsert):
        if self.head == nodeToInsert and self.tail == nodeToInsert:
            return
        self.remove(nodeToInsert)
        nodeToInsert.prev = node
        nodeToInsert.next = node.next
        if node.next is None:
            self.tail = nodeToInsert
        else:
            node.next.prev = nodeToInsert
        node.next = nodeToInsert

    # () <-> (node) <-> ()
    # O(p) time | O(1) space, p - position
    def insertAtPosition(self, position, nodeToInsert):
        if position == 1:
            self.setHead(nodeToInsert)
            return
        curr_node = self.head
        curr_position = 1
        while curr_node is not None and curr_position != position:
            curr_node = curr_node.next
            curr_position += 1
        if curr_node is not None:
            self.insertBefore(curr_node, nodeToInsert)
        else:
            self.setTail(nodeToInsert)

    # () <-> (node) <-> ()
    # O(n) time | O(1) space
    def removeNodesWithValue(self, value):
        curr_node = self.head
        while curr_node is not None:
            node_to_remove = curr_node
            curr_node = curr_node.next
            if node_to_remove.value == value:
                self.remove(node_to_remove)

    # O(1) time | O(1) space
    def remove(self, node):
        # N <--- (node) ---> N
        if node == self.head:
            self.head = self.head.next
        if node == self.tail:
            self.tail = self.tail.prev
        self.removeNodeBindings(node)

    # O(n) time | O(1) space
    def containsNodeWithValue(self, value):
        curr_node = self.head
        while curr_node is not None and curr_node.value != value:
            curr_node = curr_node.next
        return curr_node is not None

    def removeNodeBindings(self, node):
        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev
        node.prev = None
        node.next = None
