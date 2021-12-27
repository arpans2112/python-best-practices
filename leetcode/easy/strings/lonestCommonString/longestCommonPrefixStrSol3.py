class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        """
        Solution:

        1. itterate over one chracter of all the strings in array and collect in the tuple s
        2. Check len of the set is equal to 1.  if not then break the loop and note down the index
        3. if the index is not found, that means, the minnimum len string is the longest prefix.
        Boundary Cases:
        4. what if there is only one string in the given array,
        5. What if one of the string is None or empty in the array



        :param strs:
        :return:
        """
        if not all(strs):
            return ''
        elif len(strs) == 1:
            return strs[0]

        index = -1
        for i, s in enumerate(zip(*strs)):
            print(i, s)
            if len(set(s)) != 1:
                index = i
                break

        min_str_len = min([len(e) for e in strs])

        index = index if index != -1 else min_str_len

        return strs[0][:index]
