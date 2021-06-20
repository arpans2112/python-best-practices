class Person:

    def __init__(self , fname,lname):
        self.fname = fname
        self.lname = lname

    def printNames(self):
        print("my first name is {} and last name is {}".format(self.fname, self.lname))