import re


class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        """
         Test Case:
            1. min string length = 1
            2. When There is only one group
            3. There are more than one group, first group has less than < k characters
            4. There are more than one group, first group has greater > k characters.
            5. reminder of: total_no_character%k = first group.
        """
        s = s.replace('-', '').upper()

        res = len(s) % k
        output = s[:res]
        for i in range(res, len(s), k):
            output += ('-' + s[i:i + k])

        return output.lstrip('-')




