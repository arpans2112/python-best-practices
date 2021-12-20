# List objects have a sort() method that will sort the list alphanumerically, ascending, by default:
from datetime import datetime
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
# To sort descending, use the keyword argument reverse = True:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse=True)
print(thislist)


# Customize Sort Function
def myfunc(n):
    return abs(n - 50)


thislist = [100, 50, 65, 82, 23]
thislist.sort(key=myfunc)
print(thislist)

# By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters:
# Case sensitive sorting can give an unexpected result:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

# Case Insensitive sort
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key=str.lower)
print(thislist)

# Reverse will just reverse the order as it's
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key=str.lower, reverse=True)
print(thislist)

name = "arpan"
# AttributeError: 'str' object has no attribute 'reverse'
# name_reverse = name.reverse()
# print(name_reverse)

# reverse will reverse the list
name_list = list(name)
name_list.reverse()

print("Sort List of tuple")
lst = [ ('AVAX', '201221'), ('AVAX', '211221'), ('AVAX', '241221'), ('AVAX', '311221'),
             ('BNB', '070122'), ('BNB', '201221'), ('BNB', '211221'), ('BNB', '241221'), ('BNB', '280122'),
             ('BNB', '311221'), ('BTC', '070122'), ('BTC', '201221'), ('BTC', '211221'), ('BTC', '241221'),
             ('BTC', '250222'), ('BTC', '250322'), ('BTC', '280122'), ('BTC', '311221'), ('ETH', '070122'),
             ('ETH', '201221'), ('ETH', '211221'), ('ETH', '241221'), ('ETH', '250222'), ('ETH', '250322'),
             ('ETH', '280122'), ('ETH', '311221'), ('MATIC', '070122'), ('MATIC', '201221'), ('MATIC', '211221'),
             ('MATIC', '241221'), ('MATIC', '311221'), ('SOL', '070122'), ('SOL', '201221'), ('SOL', '211221'),
             ('SOL', '241221'), ('SOL', '280122'), ('SOL', '311221'),('AVAX', '070122')]


# Sort tuple list based on the pair,

from datetime import datetime
new_list = sorted(lst, key=lambda x:(x[0], datetime.strptime(x[1], '%d%m%y')))
print(new_list)

new_list1 = lst.copy()
new_list1.sort(key=lambda x:(x[0], datetime.strptime(x[1], '%d%m%y')))
print(new_list)