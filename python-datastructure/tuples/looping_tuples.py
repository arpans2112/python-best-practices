print("using each element in the for loop")
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
    print(x)


print("using indexing, with the help of range and len function")
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
    print(thistuple[i])

print("using while loop")
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
    print(thistuple[i])
    i = i + 1