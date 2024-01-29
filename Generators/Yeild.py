def cube(n):
    for x in range(n):
        yield x**3


print(list(cube(20)))


# fabbonaci number
def get_fab(n):
    a = 1
    b = 1

    for i in range(n):
        yield a
        a, b = b, a + b


print(list(get_fab(10)))
