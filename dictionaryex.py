# program to print dictionary items @pranav version 3.9
# ordered, unchangeable , and does not allow duplicates
import collections
dict1 = {"PAST": 2021, "PRESENT": 2022, "FUTURE": 2023}
print(dict1)

# to print single element in dictionary. we have to give key name and it will print the value
print(dict1["PAST"])

# to add element in dictionary
dict1["END"] = 2055
print(dict1)

# to delete an element from dictionary
dict1.pop("END")
print(dict1)

# to update an element in dictionary
dict1.update({"END": 2077})
print(dict1)

# to print undeclared element of dictionary in single line
print(dict1.get("SPACE", "INFINITE"))

# it set the default value of Universe is 1 in dict1 and it will add in dictionary
dict1.setdefault("UNIVERSE", 1)
print(dict1)

# it creates the new dictionary. lambda is anonymous keyword use to store value.
defd = collections.defaultdict(lambda : 'Key not found')
defd['Pranav'] = 1
defd['Abhijeet'] = 1
print(defd)


# to clear all element from dictionary
dict1.clear()
print(dict1)

# to delete the whole dictionary we use del keyword and hence we deleted the dictionary we cannot print it otherwise
# it will show error
del dict1