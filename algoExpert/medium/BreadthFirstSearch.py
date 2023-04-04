# Do not edit the class below except
# for the breadthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
import unittest


class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    # O(V + E) time | O(V) space
    def breadthFirstSearch(self, array):
        queue = [self]
        while len(queue) > 0:
            next_elem = queue.pop(0)
            array.append(next_elem.name)
            queue.extend(next_elem.children)
        return array


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        graph = Node("A")
        graph.addChild("B").addChild("C").addChild("D")
        graph.children[0].addChild("E").addChild("F")
        graph.children[2].addChild("G").addChild("H")
        graph.children[0].children[1].addChild("I").addChild("J")
        graph.children[2].children[0].addChild("K")
        self.assertEqual(graph.breadthFirstSearch([]), ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"])

# Ex:
#          A
#       /  |  \
#      B   C   D
#    /  \    /  \
#   E   F   G   H
#     /  \   \
#    I   J    K

# => ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"]
