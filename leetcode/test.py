import re
given_dic  = {'a':1,'b':2}

del given_dic['a']
del given_dic['b']

print(len(given_dic))


print(int('-1'))
print(int('1'))

start_index =  0 if True else 1
for i in range(start_index, len("arpan")):
    pass


txt = "The Spain rain in Spain to Spain"
match = re.search("Spain", txt)
# Return the touple of all the matches in the string
print(match.groups())
# Return the first matched string
print(match.group())
# Return the start index of the searched string
print(match.start())
# Return the end index of the searched string
print(match.end())
# Return the tuple of (start_index, end_index) of the searched string
print(match.span())
# Return the input string
print(match.string)

# print(dir(x))

txt.find("Spain")



# print(x.groups(0))




