import random

choices = ["rock", "paper", "scissors"]

while True:
    user = input("Rock, Paper, or Scissors? (or 'q' to quit): ").lower()
    if user == "q":
        break
    if user not in choices:
        print("Invalid choice.")
        continue
    computer = random.choice(choices)
    print("Computer chose:", computer)

    if user == computer:
        print("It's a tie!")
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        print("You win!")
    else:
        print("You lose!")
