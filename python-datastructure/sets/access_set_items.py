# you can't access set items by indexing


# you can use for loop for accesing set items
thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print(x)

# we can use in operator to check if element is present or not in the set.
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)

# Once a set is created, you cannot change its items, but you can add new items.
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

# combine two sets.
