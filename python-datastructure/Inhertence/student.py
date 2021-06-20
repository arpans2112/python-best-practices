from person import Person


class Student(Person):
    def __init__(self,phone_number, email , fname, lname):
        self.phone_number = phone_number
        self.email = email
        # With super you don't need to pass the self keyword
        super().__init__(fname, lname)
        # with below representation we have to use the self.
        Person.__init__(self,fname,lname)

# If you add a method in the child class with the same name as a function in the parent class,
# the inheritance of the parent method will be overridden.

student = Student(8018678792, "arpan673523@gmail.com","arpan", "saini")
student.printNames()

