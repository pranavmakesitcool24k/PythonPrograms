# create a class and a constructor in python @pranav version 3.9

class Computer:
    a = 2

    def __init__(self, aname, aage, asalary):    # parametrize constructor
        self.name = aname
        self.age = aage
        self.salary = asalary


c1 = Computer("pranav", "11", "22222")
print("1)Name: " + c1.name + "\n2)Age: " + c1.age + "\n3)Salary: " + c1.salary)
