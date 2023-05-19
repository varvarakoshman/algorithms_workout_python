import unittest


# Solution 1 (Recursive)
# O(n*2^n) time | O(n*2^n) space
def powerset_1(array):
    result = [[]]
    powerset_helper(array, 0, result)
    return result


def powerset_helper(array, idx, result):
    if idx == len(array):
        return
    for i in range(len(result)):
        existing_subset = result[i]
        result.append(existing_subset + [array[idx]])
    powerset_helper(array, idx + 1, result)


# Solution 1 (Recursive from video explanation)
# O(n*2^n) time | O(n*2^n) space
def powerset(array, idx=None):
    if idx is None:
        idx = len(array) - 1
    elif idx < 0:
        return [[]]
    subsets = powerset(array, idx - 1)
    for i in range(len(subsets)):
        existing_subset = subsets[i]
        subsets.append(existing_subset + [array[idx]])
    return subsets


# Solution 2 (Iterative)
# O(n*2^n) time | O(n*2^n) space
def powerset_2(array):
    result = [[]]
    for elem in array:
        for i in range(len(result)):
            existing_subset = result[i]
            result.append(existing_subset + [elem])
    return result


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        output = list(map(lambda x: set(x), powerset([1, 2, 3])))
        self.assertTrue(len(output) == 8)
        self.assertTrue(set([]) in output)
        self.assertTrue(set([1]) in output)
        self.assertTrue(set([2]) in output)
        self.assertTrue(set([1, 2]) in output)
        self.assertTrue(set([3]) in output)
        self.assertTrue(set([1, 3]) in output)
        self.assertTrue(set([2, 3]) in output)
        self.assertTrue(set([1, 2, 3]) in output)