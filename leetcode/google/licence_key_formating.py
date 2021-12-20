import re


class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:

        x = re.findall("[^-]", s)
        formated_str = ""

        if len(x) <= k:
            formated_str = "".join(x)
            formated_str = formated_str.upper()
            return formated_str
        else:
            no_of_chars_in_first_group = len(x) % k
            if no_of_chars_in_first_group == 0:
                no_of_chars_in_first_group = k

        first_group = x[:no_of_chars_in_first_group]
        formated_str = "".join(first_group).upper()
        left_chars = x[no_of_chars_in_first_group:]

        start_index = 0
        for end_index in range(k, len(left_chars) + k, k):
            next_group = "".join(left_chars[start_index:end_index]).upper()
            formated_str = formated_str + "-" + next_group
            start_index = end_index

        return formated_str



