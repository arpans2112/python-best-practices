import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Solution:

        Requirement :
        string must contain only =  [a-z0-9]
        reversestring and compare if they are equal


        """
        s = ''.join(filter(str.isalnum, s)).lower()
        return s == s[::-1]
