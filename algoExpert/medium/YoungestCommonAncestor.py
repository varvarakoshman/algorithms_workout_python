# This is an input class. Do not edit.
import unittest


class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None

    def addDescendants(self, *descendants):
        for descendant in descendants:
            descendant.ancestor = self


# O(d) time | O(1) space, d - depth (height) of the ancestral tree
def get_youngest_common_ancestor(top_ancestor, descendant_one, descendant_two):
    height_one = get_node_height(top_ancestor, descendant_one)
    height_two = get_node_height(top_ancestor, descendant_two)
    if height_one > height_two:
        return backtrack_ancestral_tree(descendant_one, descendant_two, height_one - height_two)
    else:
        return backtrack_ancestral_tree(descendant_two, descendant_one, height_two - height_one)


def get_node_height(top_ancestor, descendant_node):
    height = 0
    while descendant_node != top_ancestor:
        descendant_node = descendant_node.ancestor
        height += 1
    return height


def backtrack_ancestral_tree(lower_descendant, higher_descendant, diff):
    while diff > 0:
        lower_descendant = lower_descendant.ancestor
        diff -= 1
    while lower_descendant != higher_descendant:
        lower_descendant = lower_descendant.ancestor
        higher_descendant = higher_descendant.ancestor
    return lower_descendant


def new_trees():
    ancestralTrees = {}
    for letter in list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
        ancestralTrees[letter] = AncestralTree(letter)
    return ancestralTrees


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        trees = new_trees()
        trees["A"].addDescendants(trees["B"], trees["C"])
        trees["B"].addDescendants(trees["D"], trees["E"])
        trees["D"].addDescendants(trees["H"], trees["I"])
        trees["C"].addDescendants(trees["F"], trees["G"])

        yca = get_youngest_common_ancestor(trees["A"], trees["E"], trees["I"])
        self.assertTrue(yca == trees["B"])
