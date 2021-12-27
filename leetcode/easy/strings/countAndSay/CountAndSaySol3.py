count = 1
resulted_str = ''


class Solution:

    def countAndSay(self, n: int) -> str:
        """
        check count of the a number + same_number do this process to get the next number.
        111221

        """
        resulted_string = ''
        for i in range(1, n + 1):
            resulted_string = self.getCountAndSayString(resulted_string)
            # print("count : {} and resulted string : {}".format(i,resulted_string))
        return resulted_string

    def getCountAndSayString(self, resulted_string):

        if len(resulted_string) == 0:
            return '1'

        output = ''
        count = 0
        current = None

        for c in resulted_string:
            if current != c and current is not None:
                output += f"{count}{current}"
                count = 1
            else:
                count += 1
            current = c

        output += f"{count}{current}"
        return output



