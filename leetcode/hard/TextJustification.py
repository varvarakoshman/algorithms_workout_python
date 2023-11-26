from typing import (
    List,
)


# O(n * k) time | O(m) space
# n - number of words,
# k - average length of a word,
# m - maxWidth
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        start, curr_len = 0, 0
        for i in range(len(words)):
            word = words[i]
            if curr_len + len(word) > maxWidth:
                result.append(self.get_new_line(words, maxWidth, curr_len - 1, start, i))
                start = i
                curr_len = 0
            curr_len += len(word) + 1

        last_line = " ".join(words[start:])
        extra_spaces = [" "] * (maxWidth - len(last_line))
        result.append(last_line + "".join(extra_spaces))
        return result

    def get_new_line(self, words, max_width, curr_len, start, end):
        new_line = []
        words_count = end - start
        gaps_count = words_count - 1
        spaces_count = max_width - (curr_len - gaps_count)

        if gaps_count == 0:
            return words[start] + " " * spaces_count

        spaces_size = spaces_count // gaps_count
        extra_spaces_count = spaces_count % gaps_count
        for i in range(start, end - 1):
            word_with_spaces = words[i] + " " * spaces_size
            if extra_spaces_count > 0:
                word_with_spaces += " "
                extra_spaces_count -= 1
            new_line.append(word_with_spaces)

        new_line.append(words[end - 1])
        return "".join(new_line)


if __name__ == '__main__':
    solution = Solution()
    assert (solution.fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16) ==
            ["This    is    an",
             "example  of text",
             "justification.  "])

    assert (solution.fullJustify(["What", "must", "be", "acknowledgment", "shall", "be"], 16)) == \
           ["What   must   be",
            "acknowledgment  ",
            "shall be        "]

    assert (solution.fullJustify(
        ["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain", "to", "a", "computer.", "Art",
         "is", "everything", "else", "we", "do"], 20)) == \
           ["Science  is  what we",
            "understand      well",
            "enough to explain to",
            "a  computer.  Art is",
            "everything  else  we",
            "do                  "]
