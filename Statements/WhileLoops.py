x = 0
while x < 5:
    print(f"x is {x}")
    x = x + 1

# use else with while
a = 10
while a >= 0:
    print(f"a is {a}")
    a = a - 1
else:
    print("loop completed")

# use break: Breaks out of the current closest enclosing loop.
while True:
    print("welcome")
    break

# use continue: Goes to the top of the closest enclosing loop.
a = 0
for str in "harry":
    if str == "a":
        continue
    print(str)

# use pass: Does nothing at all.
for item in [1, 2, 3]:
    pass
