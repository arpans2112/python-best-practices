car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "white"

print(x) #after the change

for x in car:
    print(x)

a = car.fromkeys("brand","model")
print(a)


x = ('key1', 'key2', 'key3')
y = 0

thisdict = dict.fromkeys(x, y)
print(thisdict)

x = ('key1', 'key2', 'key3')
thisdict = dict.fromkeys(x,"arpan")
print(thisdict)