# use built in functions in class object
class Book:
    def __init__(self, book, author, pages):
        self.book = book
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.book} is written by {self.author}"

    def __len__(self):
        return self.pages


book = Book(book="Kali Vidya", author="Jaidev", pages=300)

print(book)

print(len(book))
