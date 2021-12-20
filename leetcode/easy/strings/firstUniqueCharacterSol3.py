"""

104 / 104 test cases passed.
Status: Accepted
Runtime: 4960 ms
Memory Usage: 14.4 MB
#  if c.index() == c.rindex():
#  if c.find() == c.rfind():

"""

class Solution:
    def firstUniqChar(self, s: str) -> int:

        for i, c in enumerate(s):
            if c.find() == c.rfind():
                return i
        return -1
