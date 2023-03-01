# create a program to handle exception in python @pranav version 3.9

try:
    x = ("aaa" + 2)
except:
    print("error")
finally:
    print("Check Program!")         # this block gonna executed no matter what

x = 2
y = 3
if x > y:
    print("{} is greater than {}".format(x, y))
else:
    print("Program is correct!")
    raise Exception("Jaan Buch ke error diya")         # raise keyword will occour error even if your program is correct


