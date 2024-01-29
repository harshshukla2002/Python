def add(num1, num2):
    try:
        return num1 + num2
    except:
        return "you are not adding correctly"


print(f"Sucessfully completed \n {add(1, 2)}")
print(f"Error occured \n {add(1, '2')}")


# print specific error
def write_files(work):
    try:
        f = open("testfile.txt", "w")
        f.write(work)
        print("Written Completed")
    except TypeError:
        print("Type error")
    except OSError:
        print("OSError")
    except:
        print("Other error")


write_files("This is first line")
write_files("Writing new messages")
