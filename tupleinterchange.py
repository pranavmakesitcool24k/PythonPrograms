# wap to input any two tuple and interchange the tuple variable @pranav version 3.10
t1 = tuple(input("enter first tuple "))
t2 = tuple(input("enter second tuple "))
t3 = t2
t2 = t1
print("tuple first: ", t3)
print("tuple second: ", t1)
