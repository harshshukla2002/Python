# -------------------------map-------------------------------
mylist = [1, 2, 3, 4, 5]


def square(num):
    return num**2


res = list(map(square, mylist))
print(res)

# -------------------------filter-------------------------
nums = [1, 2, 3, 4, 5, 6]


def check_even(num):
    return num % 2 == 0


result = list(filter(check_even, nums))
print(result)

# -----------------lambda Expression---------------------
cube = lambda num: num**3

result = cube(5)
print(result)
