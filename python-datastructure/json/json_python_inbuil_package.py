import json
# some JSON:

# Converting json to dictionary
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["city"])
print(y)

# Converting dictionary to json
# a Python object (dict):
x = {
    "name": "John",
    "age": 30,
    "city": "New York"
   }

# convert into JSON:
# y = json.dumps(x)
print("*"*20)
json.dumps(x, indent=4, separators=(". ", " = "))
# the result is a JSON string:
print(y)


# Converting different type of python objects to json
print("Converting different type of python objects to json")
print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))




# Convert a Python object containing all the legal data types:
print("Converting to a Python object containing all the legal data types:")
x = {
    "name": "John",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ("Ann","Billy"),
    "pets": None,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
    ]
}

# we can write the json path to get any value from the json.
json_obj = r'{"name": "John", "age": 30, "married": true, "divorced": false, "children": ["Ann", "Billy"], "pets": null, "cars": [{"model": "BMW 230", "mpg": 27.5}, {"model": "Ford Edge", "mpg": 24.1}]}'
print(json.dumps(x, indent=4))
pyobjec = json.loads(json_obj)
print(pyobjec["children"][1])
print(pyobjec["cars"][0])




