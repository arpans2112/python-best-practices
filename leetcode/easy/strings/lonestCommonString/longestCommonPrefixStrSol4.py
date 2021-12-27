class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        """
        Solution:
        compare first two string get the longest prefix, then compare the prefix with the next string and continue the process until the end of array
        if the prefix is empty in the last then there is not common prefix else the left over is the longest prefix


        :param strs:
        :return:
        """

        prefix = strs[0]

        if (len(prefix) == 0):
            return ""

        for i in range(1, len(strs)):
            builder = ''
            compare_to = strs[i]

            if (len(compare_to) == 0):
                return ""

            if len(compare_to) < len(prefix):
                compare_to, prefix = prefix, compare_to

            print("compare to : {} prefix : {}".format(compare_to, prefix))
            index = 0
            while (index < len(prefix)):
                if compare_to[index] == prefix[index]:
                    builder += prefix[index]
                else:
                    prefix = builder
                    break
                index += 1
            prefix = builder
        return prefix

