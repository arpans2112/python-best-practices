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

            "
            96% faster than others
            "

        """
        s = s.replace("-", "").upper()

        # x = re.findall("[^-]",s)
        # formated_str = ""

        if len(s) <= k:
            return s
        else:
            no_of_chars_in_first_group = len(s) % k
            if no_of_chars_in_first_group == 0:
                no_of_chars_in_first_group = k

        first_group = s[:no_of_chars_in_first_group]
        left_chars = s[no_of_chars_in_first_group:]
        start_index = 0
        formated_str = first_group
        for end_index in range(k, len(left_chars) + k, k):
            next_group = left_chars[start_index:end_index]
            formated_str += "-" + next_group
            start_index = end_index

        return formated_str



