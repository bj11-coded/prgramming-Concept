import os

# file handaling helps to change the file as reading , writting , editing and deleting
# file handaling is a important part of python programming


# to read the file we use read() function  

# open helps to open the file
# "r" is for reading the file
newFi = open("texts.txt", "w")
print(newFi.write)
files = open("texts.txt", "r")
print(files.read())
# files.close()

# ...existing code...

# to print the external file we use the same open() function with r keyword in the start 
fil = open(r"C:\Users\admire\Desktop\dummy.txt.txt", "r")
print(fil.read())
# fil.close()
# ...existing code...

# using with statement to open the file
# with statement is used to open the file and it will automatically close the file after the block of code is executed
with open("texts.txt", "r") as files:
    print(files.read())


# using readlines() to read the file line by line
# close () function is used to close the file after reading
fil = open("texts.txt", "r")
print(fil.readlines(8))   # prints the first 8 line of the file
fil.close()


# Write 

# to write in the file we use write() funciton
# open helps to open the file

# some keywords used in write 
# "w" is for writing in the file
# "a" is for appending in the file
# "x" is for creating a new file and writing in it
# "r+" is for reading and writing in the file
# "w+" is for writing and reading in the file
# "a+" is for appending and reading in the file
# "x+" is for creating a new file and reading in it


newFil = open("newFile.txt", "w")
newFil.write("This is a new file created using write function.\n")

newFil = open("newFile.txt", "a")
newFil.write("i have added new line using append 'a' keyword")
with open("newFile.txt", "r") as newFil:
    print(newFil.read())


# rmdir is used to remove directory
# os.rmdir("hero")
# os.remove("newFile.txt")

# if os.path.exists("texts.txt"):
#     os.remove("texts.txt")
# else:
#     print("no such file found")