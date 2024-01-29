def wrapper(func):
    print("line before function")
    print(func())
    print("line after function")


@wrapper
def hello():
    return "Hello world"
