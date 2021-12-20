class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        unique_strings = list()
        longest_string = ""
        longest_length = -1;
        index = -1
        longest_string_index = -1

        if s is None:
            return 0
        elif len(s) == 0:
            return 0
        elif len(s) == 1:
            return 1

        iterindex = 0

        while (iterindex < len(s)):
            c = s[iterindex]
            if c in longest_string:
                unique_strings.append(longest_string)
                index += 1
                longest_str_len = len(longest_string)
                if longest_str_len > longest_length:
                    longest_length = longest_str_len
                    longest_string_index = index;
                # print (s)
                # print(longest_string)
                s = longest_string[1:] + s[len(longest_string):]
                iterindex = 0
                longest_string = ""

            else:
                longest_string += c
                iterindex += 1

        unique_strings.append(longest_string)
        index += 1
        longest_str_len = len(longest_string)
        if longest_str_len > longest_length:
            longest_length = longest_str_len
            longest_string_index = index;

        return longest_length


