# Solution 1
# O(n! * n^2) time | O(n! * n) space
class Solution1:
    def getPermutations(self, array):
        permutations = []
        self.permutations_helper(array, [], permutations)
        return permutations

    def permutations_helper(self, array, curr_perm, permutations):
        if not len(array) and len(curr_perm):
            permutations.append(curr_perm)
        else:
            for i in range(len(array)):
                new_array = array[:i] + array[i + 1:]
                new_perm = curr_perm + [array[i]]
                self.permutations_helper(new_array, new_perm, permutations)


# Solution 2 (optimal)
# O(n! * n) time | O(n! * n) space
class Solution2:
    def getPermutations(self, array):
        permutations = []
        self.permutations_helper(0, array, permutations)
        return permutations

    def permutations_helper(self, i, array, permutations):
        if i == len(array) - 1:
            permutations.append(array[:])  # make a copy using slicing
        else:
            for j in range(i, len(array)):
                self.swap(array, j, i)
                self.permutations_helper(i + 1, array, permutations)
                self.swap(array, i, j)

    def swap(self, array, index1, index2):
        array[index1], array[index2] = array[index2], array[index1]
