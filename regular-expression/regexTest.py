
import re

txt = "The rain in Spain"
x = re.search("[ain]+", txt)


print("The first white-space character is located in position:", x.string)
print("The first white-space character is located in position:", x.group())
print("The first white-space character is located in position:", x.span())
print("The first white-space character is located in position:", x.start())
print("The first white-space character is located in position:", x.end())
print("The first white-space character is located in position:", x.endpos)
print("The first white-space character is located in position:", x.groupdict())
print("The first white-space character is located in position:", x.groups())


