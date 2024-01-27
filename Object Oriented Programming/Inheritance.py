class Animal:
    def __init__(self):
        print("Amimal Created")

    def who_i_am(self):
        print("I am Animal")

    def eat(self):
        print("I am eatting")


class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog Created")


my_dog = Dog()

my_dog.eat()
