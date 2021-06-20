from utilities import projectProperties as pp
root = pp.project_root_path
print(root)
print(root + "/resources/textFiles/fileTest.txt")
f = open(root + "/resources/textFiles/fileTest.txt")

# read line by line without using readlines() function.
print(f)
for line in f:
    print(line.strip())

# 1. Read a line at a time and set the cursor to the next line for read
# 2. It returns the string of line.
# 3. for loop on readline() will read one character at a time.
# print(f.readline())


# it will close the file
# in some cases,due to buffering you will not see the changes in file, until you close it.
f.close()


# 1.  Read the entire file from the cursor till the end.
# 2.  returns the string.
# 3.  For loop on f.read() -> will read the file character by character.
# 4.   read(n) -> it will return the n characters string from a given cursor position.
# print(f.read())
# print(f.read(5))
# print(f.read(5))


# 1. Returns a list of all lines from the current cursor position.
# 2. for loop on f.readlines() -> it will return the one line at a time
# print(f.readlines())

# for loop on file.
# for i in f.read(5):
#     print(i)