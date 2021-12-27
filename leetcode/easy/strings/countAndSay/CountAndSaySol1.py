count = 1
resulted_str = ''


class Solution:

    def countAndSay(self, n: int) -> str:
        """
        check count of the a number + same_number do this process to get the next number.
        111221

        """

        def getCountAndSayString(givenString):

            if len(resulted_string) == 0:
                return '1'

            isLastCharacterCounted = True
            index = 0
            next_string = ''
            count = 1
            while (index < len(resulted_string) - 1):
                if resulted_string[index] == resulted_string[index + 1]:
                    count += 1
                else:
                    next_string = next_string + str(count) + resulted_string[index]
                    count = 1
                    if (index == len(resulted_string) - 2):
                        isLastCharacterCounted = False

                index += 1

            if not isLastCharacterCounted:
                next_string = next_string + str(1) + resulted_string[len(resulted_string) - 1]
                count = 1
            else:
                next_string = next_string + str(count) + resulted_string[index - 1]

            return next_string

        resulted_string = ''
        for i in range(1, n + 1):
            resulted_string = getCountAndSayString(resulted_string)
            # print("count : {} and resulted string : {}".format(i,resulted_string))
        return resulted_string



