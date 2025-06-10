import random

print("Welcome to Guess the Number!")
print("I'm thinking of a number between 1 and 100.")
print("You have 5 chances to guess it.\n")

number = random.randint(1, 100)
tries = 5

while tries > 0:
    guess = int(input("Enter your guess: "))

    if guess == number:
        print("Correct! You guessed the number.")
        break
    elif guess < number:
        print("Too low.")
    else:
        print("Too high.")

    tries = tries - 1
    print("Tries left:", tries)

if guess != number:
    print("You've used all your tries.")
    print("The number was:", number)