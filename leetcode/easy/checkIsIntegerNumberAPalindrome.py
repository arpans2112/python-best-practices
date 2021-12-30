class Solution:
    def isPalindrome(self, x: int) -> bool:

        """
        Solution:

        Rules:
        1. x can be anything between -2**31 < x < x**31-1
        2. is negative number a palindrome ?
        3. any number starts ends with zero except when it's zero can't be palindrome
        4. x // 10 = gives reaminder number
        5. x % 10 = gives the last digit
        6. build a new number from the last
        7. when we get the half of the number stop there
        10. check the original left half and the result half are equal or not
        11. if equal return true
        12. if not equal return false
        13. please consider the case when both odd and even number length numbers are
        palindrome

        solution:
        example:

        must check
        121
        1221

        if x < 0 false
        if x % 10 and x !=0 false
        else
        check algorithm for palindrome, consder the above two cases
        121 and 1221.

        write your algoritm
        Test your algoritm for atleast above test cases

        x % 10 == 1
        x // 10 == 12



        """

        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        result = 0

        while (x > result):
            x, remainder = divmod(x, 10)
            result = result * 10 + remainder

        return x == result or x == result // 10







