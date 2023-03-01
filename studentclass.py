# create a class and pass value to constructor @pranav version 3.9
class Student:
    def __init__(self, name, roll, percentage):
        self.name = name
        self.roll = roll
        self.percentage = percentage


s1 = Student("Pranav", 40, 80.00)
s2 = Student("Kashav", 11, 100.00)
s3 = Student("Aryan", 31, 70.00)

print("Name: {} Roll No: {} Percentage: {}".format(s1.name, s1.roll, s1.percentage))
print("Name: {} Roll No: {} Percentage: {}".format(s2.name, s2.roll, s2.percentage))
print("Name: {} Roll No: {} Percentage: {}".format(s3.name, s3.roll, s3.percentage))


