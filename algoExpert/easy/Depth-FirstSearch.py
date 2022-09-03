class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def add_child(self, name):
        self.children.append(Node(name))

    def depth_first_search(self, array):
        array.append(self.name)
        for child in self.children:
            child.depth_first_search(array)
        return array

    # complexity: O(|v| + |e|)
    # space complexity: O(|v|)


def get_test_tree():
    node1 = Node("A")
    node2 = Node("B")
    node3 = Node("C")
    node4 = Node("D")
    node5 = Node("E")
    node6 = Node("F")
    node7 = Node("G")
    node8 = Node("H")
    node9 = Node("I")
    node10 = Node("J")
    node11 = Node("K")
    node1.children = [node2, node3, node4]
    node2.children = [node5, node6]
    node6.children = [node9, node10]
    node4.children = [node7, node8]
    node7.children = [node11]
    return node1


if __name__ == '__main__':
    assert get_test_tree().depth_first_search([]) == ["A", "B", "E", "F", "I", "J", "C", "D", "G", "K", "H"]