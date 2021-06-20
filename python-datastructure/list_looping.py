thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
    print(thislist[i])

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
    print(thislist[i])
    i = i + 1

# Looping Using List Comprehension
thislist = [1,2,3,4]
# Like a lamda expression
[print(x*2) for x in thislist]

fruits = ["apple", "banana", "cherry", "kiwi", "mango" , "amrud"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

[print(x) for x in fruits if x.startswith("a")]

# newlist = [expression for item in iterable if condition == True]
# The return value is a new list, leaving the old list unchanged.
# The condition is optional and can be omitted:
# The iterable can be any iterable object, like a list, tuple, set etc.
# newlist = [x for x in range(10)]
# newlist = [x for x in range(10) if x < 5]
# The expression is the current item in the iteration, but it is also the outcome, which you can manipulate before it ends up like a list item in the new list:
# Set all values in the new list to 'hello':
# The expression can also contain conditions, not like a filter, but as a way to manipulate the outcome:
