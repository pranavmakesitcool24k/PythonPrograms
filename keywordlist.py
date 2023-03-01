#in this program we will see some keywords which we have to avoid during variable initialization/declaration. 

#keyword is a module in python
import keyword
#builtins is a module/object in python
import builtins


#it will print all predefined keyword in python!
print(keyword.kwlist)

#it will print all predefined keyword in python! we have to use dir() because builtins is a object.
print(dir(builtins))