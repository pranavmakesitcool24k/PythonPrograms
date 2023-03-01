# create a calculator using user define functions @pranav version 3.9

def add():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Addition is: ", a + b)


def sub():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Substraction is: ", a - b)


def mul():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print("Multiplication is: ", a * b)


def div():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print("Division is: ", a / b)


d = int(input("Enter a choice: "))
if d == 1:
    add()
elif d == 2:
    sub()
elif d == 3:
    mul()
elif d == 4:
    div()
else:
    print("Enter correct choice!!")

e = input("Enter your name: ")


def thank(name):
    print("Hello {} thanks for using our program".format(name))


thank(e)
