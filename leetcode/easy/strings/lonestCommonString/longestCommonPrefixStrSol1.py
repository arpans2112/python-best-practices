class Solution:
    def longestCommonPrefix(self, strs) -> str:
        return strs[0][:next((i for i, s in enumerate(zip(*strs)) if len(set(s)) != 1),
                             len(sorted(strs, key=lambda x: len(x))[0]))]





# rough work to understand the above concept
print("test start")
strs = ["car","cir"]
t = (i for i, s in enumerate(zip(*strs)) if len(set(s)) != 1)
for i in t:
    print(i)
print("test end")

print("one line solution start")
result = strs[0][:len([i for i,s in enumerate(zip(*strs)) if len(set(s)) == 1])]
print(result)
print('one line solutino end')

t = [i for i, s in enumerate(zip(*strs)) if len(set(s)) == 1]

print("start")
for i in (i for i, s in enumerate(zip(*strs)) if len(set(s)) != 1):
    print(i)
print("end")

for i, s in enumerate(zip(*strs)):
    if len(set(s)) == 1:
        print(i,s)

# for i in t:
#     print(i)
print(t)
strs = ["car","cir"]
print("start")
t = next((i for i, s in enumerate(zip(*strs)) if len(set(s)) != 1),
                             len(sorted(strs, key=lambda x: len(x))[0]))

print(t)
print("end")


iter = next((i for i in [4,5,6,2,3,4,5] if i == 5),1)
print(iter)