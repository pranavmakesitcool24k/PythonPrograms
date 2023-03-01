# nested if else in python @pranav

var = 150
if var < 200:
    print("Expression value is less than 200")
    if var == 150:
        print("Value is 150")
    elif var == 100:
        print("Value is 100")
    elif var == 50:
        print("Value is 50")
    elif var < 50:
        print("Expression value is less than 50")
    else:
        print("Could not find true expression")

print("good bye!")
