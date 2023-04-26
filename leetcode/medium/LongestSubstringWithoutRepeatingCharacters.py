# O(n) time | O(n) space
def lengthOfLongestSubstring(s):
    unique_letters = set()
    max_len = 0
    left = 0
    for right in range(len(s)):
        if s[right] not in unique_letters:
            unique_letters.add(s[right])
        else:
            max_len = max(max_len, right - left)
            while s[right] in unique_letters:
                unique_letters.remove(s[left])
                left += 1
            unique_letters.add(s[right])
    return max(max_len, len(s) - left)


if __name__ == '__main__':
    assert lengthOfLongestSubstring("abcabcbb") == 3
    assert lengthOfLongestSubstring("bbbbb") == 1
    assert lengthOfLongestSubstring("pwwkew") == 3
    assert lengthOfLongestSubstring("abcde") == 5
    assert lengthOfLongestSubstring("abcabcbbabcd") == 4
    assert lengthOfLongestSubstring("abcdabcabcbb") == 4
    assert lengthOfLongestSubstring("a") == 1
    assert lengthOfLongestSubstring("") == 0
