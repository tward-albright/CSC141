# Taylan Ward
# 5-1 and 5-2
# pyright: basic
dog_breed = "labrador"
print("Is dog_breed == 'labrador'? True")
print(dog_breed == "labrador")

print("\nIs dog_breed == 'shitzu'? False")
print(dog_breed == "shitzu")

print("Is dog_breed != 'labrador'? False")
print(dog_breed != "labrador")

print("Is len(dog_breed) > len('shitzu')? True")
print(len(dog_breed) > len("shitzu"))

print("Is dog_breed.istitle()? False")
print(dog_breed.istitle())

secret_number = 450

print("Is secret_number divisible by 5? True")
print(secret_number % 5 == 0)

print("Is secret_number divisible by 7? False")
print(secret_number % 7 == 0)

print("Is double the secret number divisble by 4? True")
print((secret_number * 2) % 4 == 0)

print("Is secret_number > 50? True")
print(secret_number > 50)

print("Is secret_number / 10 == 40? False")
print(secret_number / 10 == 40)
