# create a program of formatting in python @pranav version 3.9

x = 22
print("The value in x is {} and it is an integer.".format(x))

a = 11
b = 29
c = 75

print("value of a = {}, b = {} and c = {}".format(a, b, c))

age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))                        # age at index 0 and name at index 1
