class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_dict = dict()
        for c in s:
            char_dict[c] = char_dict.get(c, 0) + 1

        for k, v in char_dict.items():
            if v == 1:
                return s.index(k)

        return -1

