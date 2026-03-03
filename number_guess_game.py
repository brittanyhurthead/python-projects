import random

secret_number = random.randint(1,10)
attempts = 0

while True:
    guess = int(input("Guess a number between 1 and 10:"))
    attempts += 1

    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print("You're a genius!")
        print("It took you", attempts, "attempt(s).")
        break