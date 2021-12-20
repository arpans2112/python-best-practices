"""

104 / 104 test cases passed.
Status: Accepted
Runtime: 4960 ms
Memory Usage: 14.4 MB


"""

class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i, c in enumerate(s):
            if s.count(c) == 1:
                return i
        return -1
