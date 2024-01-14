myDict = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3",
    "key4": "value4",
    "key5": "value5",
}

# get value by key
print(f"value at key 3 is {myDict['key3']}")

# to get value from nested dictionary
nestedDict = {"key1": [1, 2, 3], "key2": {"newKey1": "this is nested value"}}
print("get nested value is %r" % nestedDict["key2"]["newKey1"])

# adding a new key
myDict["key6"] = "value6"
print(f"new list after add new key {myDict}")

# mutate key value
myDict["key2"] = "vaalue2"
print(f"mutate key2 value, now new value is {myDict}")
