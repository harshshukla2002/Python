# Can create list with multiple types
myList = ["string", 00.1, 1]
print(f"List length {len(myList)}")  # return length

# get particular index element
print(f"get element in index 1 {myList[1]}")

# get element from x index - x:
print(f"get element from index 1 {myList[1:]}")

# merge two lists
myList = [1, 2, 3]
anotherList = [4, 5]
newList = myList + anotherList
print(f"concat lists {newList}")

# we can mutate list
print(f"list before mutate {anotherList}")
anotherList[1] = 6
print(f"list after mutate {anotherList}")

# add item to end of the list
newList.append(6)
print(f"append 6 in end and a new list is {newList}")

# remove element from the list
print(f"popped element is {newList.pop()} and new list is {newList}")

# remove element by passing index
print(f"popped element from index 2 is {newList.pop(2)} and new list is {newList}")

# sorting the lists
myList = [1, 3, 4, 8, 4, 2, 1]
myList.sort()
print(f"list after sorting {myList}")

# reverse the list
myList.reverse();
print(f"list after reverse {myList}")
