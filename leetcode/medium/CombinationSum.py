# O(n^target) time | O(n^target) space
class Solution:
    def combinationSum(self, candidates, target):
        result = []

        def search_combinations(curr, curr_sum, start):
            if curr_sum == target:
                result.append(curr[:])
            elif curr_sum > target:
                return
            else:
                for i in range(start, len(candidates)):
                    curr.append(candidates[i])
                    curr_sum += candidates[i]

                    search_combinations(curr, curr_sum, i)

                    curr.pop()
                    curr_sum -= candidates[i]

        search_combinations([], 0, 0)
        return result


if __name__ == '__main__':
    assert Solution().combinationSum([2, 3, 6, 7], 7) == [[2, 2, 3], [7]]
    assert Solution().combinationSum([2, 3, 5], 8) == [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
    assert Solution().combinationSum([2], 1) == []
