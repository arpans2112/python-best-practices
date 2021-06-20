a = "arpan"
b = "abcba"


def isstringpalindrome(givenstring):
    if givenstring == givenstring[::-1]:
        return True
    else:
        return False


print(isstringpalindrome(a))
print(isstringpalindrome(b))
