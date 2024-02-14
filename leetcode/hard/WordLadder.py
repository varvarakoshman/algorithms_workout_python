# O(n * m^2) time | O(n * m^2) space
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        level = 1
        adj_list = self.build_adj_list(wordList, beginWord)
        seen = {beginWord}
        queue = [beginWord]
        while queue:
            level_count = len(queue)
            for _ in range(level_count):
                curr_word = queue.pop(0)
                if curr_word == endWord:
                    return level
                word_patterns = self.generate_word_patterns(curr_word)
                self.add_neighbours_in_queue(adj_list, word_patterns, seen, queue)
            level += 1
        return 0

    def build_adj_list(self, wordList, beginWord):
        adj_list = {}
        for word in wordList:
            self.add_word_to_list(word, adj_list)
        self.add_word_to_list(beginWord, adj_list)
        return adj_list

    def add_word_to_list(self, word, adj_list):
        for i in range(len(word)):
            pattern = word[:i] + '*' + word[i + 1:]
            if pattern not in adj_list:
                adj_list[pattern] = [word]
            else:
                adj_list[pattern].append(word)

    def generate_word_patterns(self, curr_word):
        patterns = []
        for i in range(len(curr_word)):
            patterns.append(curr_word[:i] + '*' + curr_word[i + 1:])
        return patterns

    def add_neighbours_in_queue(self, adj_list, word_patterns, seen, queue):
        neighbours = []
        for pattern in word_patterns:
            possible_neighbours = adj_list[pattern]
            for neigh in possible_neighbours:
                if neigh not in seen:
                    neighbours.append(neigh)
                    queue.append(neigh)
                    seen.add(neigh)
        return neighbours
