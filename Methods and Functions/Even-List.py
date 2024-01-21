# return if any of the number in list present or not
def check_even_list(myList):
    for value in myList:
        if value % 2 == 0:
            return True


myList = [1, 3, 5, 7, 8, 9, 11, 13]

if check_even_list(myList):
    print("even Present in the list")
else:
    print("even Not Present in the list")
