# -----------------------------range------------------------------

# we can print number using giving starting and ending index, if we pass only single argument then it will run from 0 to end - range(end) / range(start,end)
print("numbers from 1 to 10")
for num in range(1, 10):
    print(num)

print("numbers from 1 to 10 of step size 3")
# we can also pass step size
for num in range(1, 10, 3):
    print(num)

# we can generate number using range
newList = list(range(1, 10, 2))
print(newList)

# -----------------------enumerator------------------------

# we can get index and word at same time using this
word = "abcde"

for index, letter in enumerate(word):
    print(f"at {index} letter is {letter}")

# ---------------------zip--------------------------------

# we can merge two list together
list1 = [1, 2, 3]
list2 = ["a", "b", "c"]
for item in zip(list1, list2):
    print(item)

# -----------------------in------------------------------

# check if some element is present in list or not
print(1 in [1, 2, 3])  # true
print(5 in [1, 2, 3])  # false

# in string
print("a" in "harsh")

# in object
print("key4" in {"key1": "value1", "key2": "value2", "key3": "value3"})

# checking for particular key or values
d = {"key1": "value1", "key2": "value2", "key3": "value3"}
print("key1" in d.keys())
print("value1" in d.values())

# -------------------------min---------------------------------------

print(min([1, 2, 3, 4]))

# ------------------------max------------------------------
print(max([1, 2, 3, 4]))

# ----------------------------shuffle from random ------------------
from random import shuffle

myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
shuffle(myList)
print(myList)

# it doesn't return anything
randomList = shuffle(myList)
print(randomList)  # doesn't work

# ---------------------------randint--------------------
from random import randint

print(randint(1, 10))  # return value between 1 to 10

# ---------------------------input-------------------------
name = input("Enter Name: ")
print(f"nice to meet you {name}")
print(type(name))  # return always string type

# can convert it using multiple func
value = input("enter a number: ")
print(f"you enter {value}")
print(f"from {type(name)} to float {float(value)}")  # to float
print(f"from {type(name)} to int {int(value)}")  # to int

# ----------------------not in------------------------
print("a" not in "harsh")
