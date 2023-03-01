# create a program to discount on different offers @pranav version 3.10

a = int(input("enter a amount: "))
if a >= 1000 and a <= 2000:
    a = (a - a / 10)
    print("10% discount final amount: ", a)
elif a >= 2001 and a <= 5000:
    a = (a - a / 20)
    print("20% discount final amount: ", a)
elif a >= 5001:
    a = (a - a / 30)
    print("30% discount final amount: ", a)
else:
    print("no discount")
