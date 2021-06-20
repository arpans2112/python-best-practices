abc_int = {1,2,3,4}
abc_float = {1.2,2,3.11,4}
abc_string = {'arpan', 'sanjay','anil', 'kiran'}

# len() :
print(len(abc_int))

# type():
print(type(abc_float))
print(type(abc_string))
print(type(abc_int))

# update() : the update() method that inserts all the items from one set into another:
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
# thisset_new_Set = thisset + tropical : this opertor doesn't work on sets.
print(thisset)
# print(thisset_new_Set)


# The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)


# remove() :
# Note: If the item to remove does not exist, remove() will raise an error.
print("Remve element")
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

# discard(): deosn't raise an element if the element doesn't exist.
thisset = {"apple", "banana", "cherry"}
thisset.discard("arpan")
print(thisset)

# Note: If the item to remove does not exist, discard() will NOT raise an error.
# what if the element doesn't exist in the set.

# pop(): Note: Sets are unordered, so when using the pop() method, you do not know which item that gets removed.
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)

# clear() : it will empty the set, set will still exist
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

# The del keyword will delete the set completely:
thisset = {"apple", "banana", "cherry"}
del thisset
# print(thisset)

# union() :method returns a new set with all items from both sets:
# Both union() and update() will exclude any duplicate items.
# You can use the union() method that returns a new set containing all items from both sets. it doesn't affects the existing sets
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)
print(set1)


# The intersection_update() method will keep only the items that are present in both sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)


# The intersection() method will return a new set, that only contains the items that are present in both sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z)

# x.symmetric_difference_update(y): The symmetric_difference_update() method will keep only the elements that are NOT present in both sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)


# symmetric_difference
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)


