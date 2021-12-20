class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxLengthOfSet = len(set(s))
        # length of the set of unique characters
        if maxLengthOfSet == len(s):
            # if the length of the set is equal to the length of the string, then the string has no repeating characters
            return len(s)  # return the length of the string

        if len(s) == 0:  # if the string is empty, then return 0
            return 0

        subString = ''  # initialize the substring

        lengthOfCurrentSubstring = 0  # initialize the length of the current substring
        longestSubStringLength = 0  # initialize the length of the longest substring

        for i in range(len(s)):  # iterate through the string
            if s[i] in subString:  # if the current character is in the substring
                subString = subString.split(s[i])[1] + s[i]  # remove the character from the substring
                lengthOfCurrentSubstring = len(subString)  # update the length of the current substring
            else:  # if the current character is not in the substring
                subString = subString + s[i]  # add the character to the substring
                lengthOfCurrentSubstring = len(subString)  # update the length of the current substring
                if lengthOfCurrentSubstring > longestSubStringLength:  # if the length of the current substring is greater than the length of the longest substring
                    longestSubStringLength = lengthOfCurrentSubstring  # update the length of the longest substring
                    if lengthOfCurrentSubstring == maxLengthOfSet:  # if the length of the current substring is equal to the length of the set of unique characters
                        return longestSubStringLength  # return the length of the longest substring
        return longestSubStringLength  # return the length of the longest substring



