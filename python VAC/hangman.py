import random

# List of words defined in the code
words = ["python", "banana", "hangman", "india", "college", "laptop", "chai", "cycle", "monsoon", "train"]

# Choose a random word
word = random.choice(words)

tries = 6
guessed = set()

while tries > 0:
    display = ''.join([c if c in guessed else "_ " for c in word])
    print("Word:", display)

    if "_" not in display:
        print("You won!")
        break

    guess = input("Enter a letter: ")

    if guess in word:
        guessed.add(guess)
    else:
        tries -= 1
        print("Wrong guess. You have", tries, "attempts left.")

else:
    print("You lose. The word was:", word)
