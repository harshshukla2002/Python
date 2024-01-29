is_int = False
while is_int == False:
    try:
        num = int(input("Please enter a number: "))
        is_int = True
    except:
        print("opps! this is not a number")
    else:
        print("This is a number")
