a = int(input("Enter marks for math "))
b = int(input("Enter marks for english "))
c = int(input("Enter marks for marathi "))
d = int(input("Enter marks for science "))

e = a + b + c + d
f = int(e / 400 * 100)
if 100 >= f >= 80:
    print("Your grade is A")
elif 80 >= f >= 70:
    print("Your grade is B")
elif 70 >= f >= 50:
    print("Your grade is C")
elif 50 >= f >= 30:
    print("Your grade is C")
else:
    print("Your are fail!")
