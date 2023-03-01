# create an inheritence in python @pranav version 3.9
# inheritence means parent and child relation like class and object

class Person:                                    # Parent class
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def printname(self):
        print(self.fname, self.lname)


class Student(Person):                          # Child class
    pass


x = Person("Pranav", "Pardeshi")         # sending arguments to Parent class
x.printname()
x = Student("Angel", "Infotech")         # sending arguments to Child class
x.printname()
