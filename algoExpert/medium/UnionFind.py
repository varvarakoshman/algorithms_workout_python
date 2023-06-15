import unittest


# Solution 1
# brute force
class UnionFind1:
    def __init__(self):
        self.parents = {}

    # O(1) time | O(1) space
    def createSet(self, value):
        self.parents[value] = value

    # O(n) time | O(1) space
    def find(self, value):
        if value not in self.parents:
            return None

        curr_parent = value
        while curr_parent != self.parents[curr_parent]:
            curr_parent = self.parents[curr_parent]

        return curr_parent

    # O(n) time | O(1) space
    def union(self, valueOne, valueTwo):
        if valueOne not in self.parents or valueTwo not in self.parents:
            return

        representative_one = self.find(valueOne)
        representative_two = self.find(valueTwo)
        if representative_one != representative_two:
            self.parents[representative_two] = representative_one


############################################################################################

# Solution 2
# slightly optimized (with ranks)
class UnionFind2:
    def __init__(self):
        self.parents = {}
        self.ranks = {}

    # O(1) time | O(1) space
    def createSet(self, value):
        self.parents[value] = value
        self.ranks[value] = 0

    # O(logn) time | O(1) space
    def find(self, value):
        if value not in self.parents:
            return None

        curr_parent = value
        while curr_parent != self.parents[curr_parent]:
            curr_parent = self.parents[curr_parent]

        return curr_parent

    # O(logn) time | O(1) space
    def union(self, valueOne, valueTwo):
        if valueOne not in self.parents or valueTwo not in self.parents:
            return

        representative_one = self.find(valueOne)
        representative_two = self.find(valueTwo)
        if self.ranks[representative_one] > self.ranks[representative_two]:
            self.parents[representative_two] = representative_one
        elif self.ranks[representative_one] < self.ranks[representative_two]:
            self.parents[representative_one] = representative_two
        else:
            self.parents[representative_two] = representative_one
            self.ranks[representative_two] += 1


############################################################################################
# Solution 3
# optimal solution with inverse Ackerman function
class UnionFind3:
    def __init__(self):
        self.parents = {}
        self.ranks = {}

    # O(1) time | O(1) space
    def createSet(self, value):
        self.parents[value] = value
        self.ranks[value] = 0

    # O(α(n)) ~ O(1) time | O(α(n)) ~ O(1) space
    def find(self, value):
        if value not in self.parents:
            return None

        while value != self.parents[value]:
            self.parents[value] = self.find(self.parents[value])
            value = self.parents[value]

        return self.parents[value]

    # O(α(n)) ~ O(1) time | O(α(n)) ~ O(1) space
    def union(self, valueOne, valueTwo):
        if valueOne not in self.parents or valueTwo not in self.parents:
            return

        representative_one = self.find(valueOne)
        representative_two = self.find(valueTwo)
        if self.ranks[representative_one] > self.ranks[representative_two]:
            self.parents[representative_two] = representative_one
        elif self.ranks[representative_one] < self.ranks[representative_two]:
            self.parents[representative_one] = representative_two
        else:
            self.parents[representative_two] = representative_one
            self.ranks[representative_two] += 1


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        solutions = [UnionFind1(), UnionFind2(), UnionFind3()]
        for solution in solutions:
            self.assertTrue(solution.find(1) is None)
            solution.createSet(1)
            self.assertTrue(solution.find(1) == 1)
            solution.createSet(5)
            self.assertTrue(solution.find(1) == 1)
            self.assertTrue(solution.find(5) == 5)
            solution.union(5, 1)
            self.assertTrue(solution.find(5) == solution.find(1))
