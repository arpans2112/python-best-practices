s = "arpan"
i = 1
f = 1.3
fruits_name = ["apple" , "mango" , "bnana"]
detaildictionary = {
    "name" : "sanjiv",
    "PhoneNumber" : 801867879,
    "email_address": "sanjiv@gmail.com"
}

friends = {
   "sanjiv" :  {"name" : "sanjiv",
    "PhoneNumber" : 801867879,
    "email_address": "sanjiv@gmail.com"},
    "arpan" : {"name" : "arpan",
               "PhoneNumber" : 801867875,
               "email_address": "arpan@gmail.com"},
    "udit" : {"name" : "udit",
               "PhoneNumber" : 801867877,
               "email_address": "udit@gmail.com"},
}

print(fruits_name[0])
print(len(fruits_name))

print(friends["udit"]["PhoneNumber"])

for i in fruits_name:
    if i.startswith("a"):
        print(i)

print()
