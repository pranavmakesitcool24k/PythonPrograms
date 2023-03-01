# create a program to make a JSON file @pranav version 3.9
# JSON - JavaScript Object Notation
import json

# a Python object (dict):
x = {
  "name": "Pranav",
  "age": 20,
  "city": "Aurangabad"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)