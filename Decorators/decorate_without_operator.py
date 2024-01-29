def hello():
    return "Hello world"


def wrapper(func):
    print("line before function")
    print(func())
    print("line after function")


wrapper(hello)
