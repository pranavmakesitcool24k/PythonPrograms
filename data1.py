# create a simple database using MongoDB in python @pranav version 3.9
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")  # connection string got from mongodb software
print(client)  # checking mongodb is connected or not
db = client['Pranav']  # client name
collection = db['Students']  # collection name  db[table name]
list1 = [  # created a list of dictionary
    {'Name': 'Aniket', 'Location': 'Delhi', 'Marks': 80},
    {'Name': 'Om', 'Location': 'Mumbai', 'Marks': 70},
    {'Name': 'Pratik', 'Location': 'Kolkata', 'Marks': 60},
    {'Name': 'Kaveri', 'Location': 'Aurangabad', 'Marks': 100}
]

# collection.insert_many(list1)

# insert_many() will help to add multiple data in once. have to comment this part coz as many times you run this
# line it will insert data in your database.

finddata = collection.find_one()  # you can find data in your database if no parameter given it will show random data.
print(finddata)
finddata = collection.find_one({'Name': 'Kaveri'})    # to find specific data. capital/small words matter here!
print(finddata)

alldocs = collection.find({'Name': 'Om'})   # to find same data we use find() and to print we use for loop.
for item in alldocs:
    print(item)
    print('\t')


prev = {"Name": "Aniket"}                               # previous data in database
change = {"$set": {"Name": "Abhijeet"}}                 # new data in the place on previous data in database
updatedata = collection.update_one(prev, change)        # updatedata is variable and update_one(previous, new) is method

# updatedata = collection.update_many(prev, change)     # update_many(previous, new) will update more than one data
"""
current = {"Name": "Om"}
collection.delete_one(current)      # it will delete the single data from database
collection.delete_many(current)     # it will delete multiple data from database
"""
