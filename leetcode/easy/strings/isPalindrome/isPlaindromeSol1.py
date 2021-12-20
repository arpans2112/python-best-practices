import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Solution:

        Requirement :
        string must contain only =  [a-z0-9]
        reversestring and compare if they are equal


        """

        s = s.lower()
        s = re.findall("[a-z0-9]", s)
        s = ''.join(s)
        return s == s[::-1]