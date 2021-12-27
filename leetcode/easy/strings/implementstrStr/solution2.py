import re


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        Solution:
        1. if value is not present return -1
        2. Return the index of the needle in the hay stack
        3. if needle = empty or none, return 0
        4. Haystack.length or needle.length can be zero
        5. haystack and neele both are made of lowercase
        """

        if len(needle) == 0:
            return 0

        return haystack.find(needle)