"""
1. sort both the strings. and compare
2. use one dictionary : increment the counter for ever character in s and decrement character in t. where ever counter
 < 0 then stop else check in the end all values should be zero
3. Compare the counts in two dictionary.
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

