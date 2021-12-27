def crazy(words,n):
    return "".join([letter * n for letter in words])



def crazy1(words):
    for letter in words:
        new = "".join([letter*3 for letter in words])
        return new


print(crazy("arpan",3))
print(crazy1("arpan"))
