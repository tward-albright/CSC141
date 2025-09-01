# Taylan Ward
# Number guessing game

from random import randint

secret_number = randint(1, 100)
guess = 0

while guess != secret_number:
    print("Guess a number: ", end="")
    guess = int(input())

    if guess > secret_number:
        print("Over!")
    else:
        print("Under!")

print(f"You did it! The number was {secret_number}!")
