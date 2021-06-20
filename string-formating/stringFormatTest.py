# add place holder in a template
price = 49
txt = "The price is {} dollars"
print(txt.format(price))

# Format the price to be displayed as a number with two decimals:
txt = "The price is {:.2f} dollars"
print(txt.format(price))

# Multiple Values
txt = "My first name is : {} and the last name is {}"
print(txt.format("arpan","saini"))

txt = "My first name is : {1} and the last name is {0}"
print(txt.format("arpan","saini"))

# if want to place the value at more than one place
age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))

# Named index
myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))