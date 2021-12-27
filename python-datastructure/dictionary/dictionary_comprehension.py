L = [1, 2, 3, 4, 5, 3, 8, 9, 9, 8, 9]

index_dict = {}
for index, value in enumerate(L):
    index_dict.setdefault(n,[]).append(i)

R = dict()
for i,n in enumerate(L):
    R.setdefault(n,[]).append(i)
R = {n:rep for n,rep in R.items() if len(rep)>1}





r = {}
for i, n in enumerate(L):
    r.setdefault(n,[]).append(i)
print(r)


# collection to get counter dictioary
from collections import Counter
counts_dictionary = Counter(L)
R = {}
print(counts_dictionary)
for i,n in enumerate(L):
    if counts_dictionary[n]>1:
       R.setdefault(n,[]).append(i)

print(R)


# How to create a dictionary using dictionary comprehension
l = [1, 2, 3, 4, 5, 3]
dict = {index:value for index,value in enumerate(l) if value == 3}
print(dict)
