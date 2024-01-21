# args - allow us to pass many arguments without getting any error

# it create tuples and store values in it


def agrs_func(*args):
    return sum(args)


print(agrs_func(1, 2, 4, 90))

# kwargs - allow us to pass many arguments without getting any error

# it creates dictonaries and store value in it


def kwargs_func(**kwargs):
    if "fruit" in kwargs:
        print(f"my choice is {kwargs['fruit']}")
    else:
        print("there is no fruit")


kwargs_func(fruit="apple")

# use both at same function


def create_order(*args, **kwargs):
    print(f"my order is {args[0]} {kwargs['pizza']}")


create_order(2, pizza="pizza")
