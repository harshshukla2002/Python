class Dog:
    def __init__(self, breed, name, year):
        # this is attribute assignment
        self.breed = breed
        self.name = name
        self.year = year

    # method
    def bark(self):
        print("WOOF!")


my_dog = Dog(breed="Desi", name="Cherry", year=3)
print(
    f"My dog name is {my_dog.name} she is {my_dog.year}year old and she is {my_dog.breed} breed."
)

my_dog.bark()
