word = "hello"

wordList = [letter for letter in word]
print(wordList)

# generate words
numList = [num for num in range(1, 10)]
print(numList)

# generate square of numbers
squareList = [num**2 for num in range(1, 10)]
print(squareList)

# generate even of numbers
evenList = [num for num in range(1, 10) if num % 2 == 0]
print(evenList)
