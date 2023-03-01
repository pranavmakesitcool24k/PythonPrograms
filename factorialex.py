# write a program to calculate factorial of given number using function


def factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact = fact * i
    return fact


number = int(input("Please enter any number to find factorial: "))
result = factorial(number)
print("The factorial of {} = {}".format(number, result))
