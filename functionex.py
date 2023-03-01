
# program to create a function in python @pranav version 3.9

# single parameter
def myfunction(name):
    print("Dr " + name)


myfunction("Salunke")
myfunction("Tiwari")
myfunction("Sharma")


# double parameter
def my_function(fname, lname):
    print(fname + " " + lname)


my_function("Pranav", "Pardeshi")


# If the number of arguments is unknown, add a * before the parameter name

def my_function(*kids):
    print("The youngest child is " + kids[2])


my_function("Emil", "Tobias", "Linus")

# function with three parameters

def my_function(child3, child2, child1):
  print("The older child is " + child1)


my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

# having an empty function definition like this, would raise an error without the pass statement

def myfunction():
  pass
