# class example in python @pranav version 3.9
class MyClass:
    x = 5


# calling the value of class outside the class
p1 = MyClass()
print(p1.x)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("John", 36)

print(p1.name)
print(p1.age)
