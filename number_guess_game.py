import random

difficulty = input("Choose difficulty (easy/medium/hard):").lower()

if difficulty == "easy":
    max_number = 10
    max_attempts = 3
elif difficulty == "medium":
    max_number = 20
    max_attempts = 7
elif difficulty == "hard":
    max_number = 50
    max_attempts = 10
else:
    print("Invalid choice. Defaulting to easy level.")
    max_number = 10
    max_attempts = 3

secret_number = random.randint(1,max_number)
attempts = 0

while attempts < max_attempts:
    try:
        guess = int(input(f"Guess a number between 1 and {max_number}:"))
    except ValueError:
        print("Please enter a valid number.")
    continue

    attempts += 1

    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print("You're a genius!")
        print("It took you", attempts, "attempt(s).")
        break