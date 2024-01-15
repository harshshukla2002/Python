myList = [1, 2, 3, 4, 5, 6]
for num in myList:
    print(num)

# iterate on nested lists
myNestedList = [[1, 2], [3, 4], [5, 6]]
for [a, b] in myNestedList:
    print(a, b)

# iterate on dictionaries
myDict = {"k1": 1, "k2": 2, "k3": 3}
for item in myDict.items():
    print(item)

# want on values
for value in myDict.values():
    print(value)

# want on keys
for key in myDict.keys():
    print(key)

# nested for loops
nestedLoopList = []
for x in [1, 2, 3]:
    for y in [4, 5, 6]:
        nestedLoopList.append(x * y)

print(nestedLoopList)
