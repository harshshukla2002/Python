from random import shuffle


def guess_game():
    cups = [" ", "O", " "]
    shuffle(cups)
    guess = player_guess()

    if cups[guess] == "O":
        print("wow Correct!")
    else:
        print("oops wrong!!")
        print(f"list is {cups}")


def player_guess():
    guess = ""
    while guess not in ["0", "1", "2"]:
        guess = input("Pick a number 0 1 or 2 : ")

    return int(guess)


guess_game()
