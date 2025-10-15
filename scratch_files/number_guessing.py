from random import randint

answer = randint(1, 100)
guess = -1

while guess != answer:
    guess = int(input("What number do you guess? > "))
    if guess > answer:
        print("Too high!")
    elif guess < answer:
        print("Too low!")
print("You win!")
