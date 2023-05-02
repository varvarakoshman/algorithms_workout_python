# O(n) time | O(n) space
class Solution(object):
    def topKFrequent(self, nums, k):
        frequencies = {}
        max_freq = 0
        for num in nums:
            frequencies[num] = frequencies.get(num, 0) + 1
            max_freq = max(max_freq, frequencies[num])
        indices = self.map_freq_to_indices(frequencies, max_freq)
        return self.get_k_elements(indices, k)

    def map_freq_to_indices(self, frequencies, max_freq):
        indices = [None] * (max_freq + 1)
        for num, freq in frequencies.items():
            if indices[freq] is None:
                indices[freq] = [num]
            else:
                indices[freq].append(num)
        return indices

    def get_k_elements(self, indices, k):
        result = []
        for i in range(len(indices) - 1, 0, -1):
            if indices[i] is not None:
                for elem in indices[i]:
                    if len(result) == k:
                        return result
                    result.append(elem)
        return result


if __name__ == '__main__':
    assert Solution().topKFrequent([1, 1, 1, 2, 2, 3], 2) == [1, 2]
    assert Solution().topKFrequent([1], 1) == [1]
    assert Solution().topKFrequent([1, 1, 2, 2, 3, 3, 4, 4], 2) == [1, 2]
    assert Solution().topKFrequent([1, 1, 2, 2, 3, 3, 4, 4], 1) == [1]
    assert Solution().topKFrequent([1, 1, 2, 2, 3, 3, 4, 4], 4) == [1, 2, 3, 4]
