thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

# Replace Item value at a given index.
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

# Change a Range of Item Values
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

# Change a Range of Item Values, where range < elements in the list added
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

# Change a Range of Item Values, where range > elements in the list added
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

# Insert a new element in the list
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)


# add element in the list
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

# Extend List : list passed as an argument will be added in the last
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

# extend the set
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)


# extend the the set
print("extend the the set")
thislist = ["apple", "banana", "cherry"]
thisset = set(("kiwi", "orange"))
thislist.extend(thistuple)
print(thislist)

print("extend the the dict: it will add the keys of the dict in the last ")
thislist = ["apple", "banana", "cherry"]
thisdict = {"kiwi":"fruit", "orange":"juice"}
thislist.extend(thistuple)
print(thislist)


# Remove item
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

# Remove Specified Index
# pop removed from the specified index, default it will remove from the last
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

# The del keyword also removes the specified index:
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

# Delete the entire List
thislist = ["apple", "banana", "cherry"]
del thislist
# print(thislist)

# clear will clear the list
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)




