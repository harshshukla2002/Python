Str = "red"
print(Str)

# want multiple quotes-
newStr = "I'm saved"
print(newStr)

# want to print char in new line
print("hello \n harsh")

# to get length
length = len("save")
print(length)

# indexing
myStr = "hello"
print(myStr[2])  # positive indexing
print(
    myStr[-3]
)  # negative indexing (0,...-3,-2,-1 - start form 0 but have end with -1)

# slicing
myStr = "abcdefgh"
print(myStr[2:])  # if we want after index - x:
print(myStr[:3])  # if we want before index - :x
print(myStr[1:3])  # if we want between indexes - x:y
print(myStr[::2])  # if we want step on char ::x
print(myStr[1:5:2])  # if we want step on char and also between indexes x:y:step
print(myStr[::-1])  # if want to reverse string using step size

# immutability - we cannot assign any thing in already present index using index
Str = "string"
# Str[2] = "e"  # error because we cannot change this

# concatinate string
Str = "Hey"

print(Str + " Harsh")

# string methods

print(Str.upper())  # turn in upper case
print(Str.lower())  # turn in lower case
print(Str.split())  # split string and convert in array
print(
    Str.split("e")
)  # pass a argument so it remove that string and then return a splited string and convert it an array

print(
    "this is best {}".format("version")
)  # .format is used insert other string in between string

print("hey, {} {} {} here".format("glad", "you", "are"))  # pass multiple string
print(
    "hey, {2} {0} {1} here".format("glad", "you", "are")
)  # pass parameter for print according to index
print(
    "hey, {g} {y} {a} here".format(g="glad", y="you", a="are")
)  # pass parameter for print according to variable name

const = 12 / 9

print(
    "the const value is {c:1.2f}".format(c=const)
)  # we can format like value:width.precision f (float formatting)
print(
    "the const value is {c:10.2f}".format(c=const)
)  # we can format like value:width.precision f we can make more width by pass max value

# another way to concate string
name = "Harsh Shukla"
print(f"My name is {name}")

# formatting with placeholder
print("Hey Come %s and %s shit" % ("here", "clean"))
