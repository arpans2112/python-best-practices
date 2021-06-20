# A tuple is a collection which is ordered and unchangeable.
mytuple = ("apple", "banana", "cherry")
print(mytuple)

# it returns the datatype as string, this is not the way of created tuple with single element
single_el_tuple = ("arpan")
print(single_el_tuple)
print(type(single_el_tuple))

# Create tuple with single element.
single_el_tuple_right = (1,)
print(single_el_tuple_right)
print(type(single_el_tuple_right))



# All type are of String type
str_mytuple = ("apple", "banana", "cherry")
print(type(str_mytuple))
int_mytuple = (1,2,3)
print(type(int_mytuple))
float_mytuple = (1.23, 1, 35, 3.5)
print(type(float_mytuple))

# it is also possible to use the tuple() constructor to make a tuple.
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

# indexing follow the same rule as in string indexing.

# Check if element exist in tuple, we use in operator.
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
    print("Yes, 'apple' is in the fruits tuple")

if "apple" not in thistuple:
    print("Yes, 'apple' is in the fruits tuple")
else:
    print("apple is not in tuple")

# unpacking a tuple:
# he number of variables must match the number of values in the tuple,
# if not, you must use an asterix to collect the remaining values as a list.
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green,yellow,red, sep='|')
# apple|banana|cherry

# Three different version of astrastics
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green,yellow,red)
# apple banana ['cherry', 'strawberry', 'raspberry']

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green,tropic,red)
# apple ['mango', 'papaya', 'pineapple'] cherry

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(*green, tropic, red) = fruits
print(green,tropic,red)
# ['apple', 'mango', 'papaya'] pineapple cherry









