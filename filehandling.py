import os
# create a file handling program in python @pranav version 3.9

f = open("file.text", "w")
f.write("This is first file handling program!")
print("data inserted successfully!")
f.close()

if os.path.exists("file.text"):
    os.remove("file.text")
else:
    print("File not exist!")

# os.mkdir("FileHandling")
if os.path.exists("FileHandling"):
    os.rmdir("FileHandling")
else:
    print("Folder not exist!")
