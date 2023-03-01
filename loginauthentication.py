# authentication program to check valid user @pranav
a = "pranav"
b = "pass@123"

c = input("Enter Username: ")
d = input("Enter Password: ")

if a == c and b == d:
    print("Valid User: ", a)
else:
    print("Invalid User")
