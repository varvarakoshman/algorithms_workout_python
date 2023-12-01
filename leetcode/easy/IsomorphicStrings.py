# O(n) time | O(1) space
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_to_t_mapping = {}
        t_to_s_mapping = {}
        for i in range(len(s)):
            if s[i] in s_to_t_mapping or t[i] in t_to_s_mapping:
                is_isomorphic = s[i] in s_to_t_mapping and t[i] in t_to_s_mapping \
                and s_to_t_mapping[s[i]] == t[i] and t_to_s_mapping[t[i]] == s[i]
                if not is_isomorphic:
                    return False
            else:
                s_to_t_mapping[s[i]] = t[i]
                t_to_s_mapping[t[i]] = s[i]
        return True


# O(n) time | O(n) space
class Solution2:
    def transformString(self, s: str) -> str:
        index_mapping = {}
        new_str = []
        for i, c in enumerate(s):
            if c not in index_mapping:
                index_mapping[c] = i
            new_str.append(str(index_mapping[c]))

        return " ".join(new_str)

    def isIsomorphic(self, s: str, t: str) -> bool:
        return self.transformString(s) == self.transformString(t)


if __name__ == '__main__':
    solution = Solution()
    assert solution.isIsomorphic("egg", "add") is True
    assert solution.isIsomorphic("foo", "bar") is False
    assert solution.isIsomorphic("paper", "title") is True
    assert solution.isIsomorphic("badc", "baba") is False
