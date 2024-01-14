myFile = open("working.txt")

# read
print("reading the file %r" % myFile.read())

print("reading the file with error %r" % myFile.read())
# shows empty string we need to restart

# we need to seek if want to read again file
myFile.seek(0)
print("reading the file again after seek %r" % myFile.read())

# we can get back values in list format
myFile.seek(0)
print("reading the file in list format %r" % myFile.read())

# we can also close files
myFile.close()

# we can read file using with method so that we don't need to worry about closing the file
with open("working.txt") as myfile:
    content = myfile.read()

print("reading the file using with method %r" % content)

# more method in open
with open("working.txt", mode="r") as myfile:  # mode which defines read and write
    content = myfile.read()

    print("reading with mode r %r" % content)

# mode = 'w' - write only
# mode = 'r' - write only
# mode = 'r+' - read and write
# mode = 'w+' - write and read

# append in file
with open("working.txt", mode="a") as myfile:
    myfile.write("\n This is line 4.")

# reading again after append
with open("working.txt", mode="r") as myfile:
    content = myfile.read()

    print("reading again after append %r" % content)

# creating a new file
with open("new_file.txt", mode="w") as myfile:
    myfile.write("\n This is new File")

with open("new_file.txt", mode="r") as myfile:
    content = myfile.read()

    print("reading a new file %r" % content)
