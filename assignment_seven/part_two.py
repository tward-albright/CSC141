# 7-4
while True:
    topping = input("Enter a pizza topping or 'q' to quit: ").lower()
    if topping == "q":
        break
    print(f"Adding {topping} to your pizza...")

# 7-5
while True:
    age = int(input("How old is the purchaser (-1 to quit)? "))
    if age == -1:
        break
    elif age < 3:
        print("Your ticket is free!")
    elif age > 12:
        print("Your ticket is $15.")
    else:
        print("Your ticket is $10.")

# 7-6
amount = 7
while amount > 0:
    amount -= 1
    topping = input("Enter a pizza topping or 'q' to quit: ").lower()
    if topping == "q":
        break
    print(f"Adding {topping} to your pizza...")

# 7-7
while True:
    print("Hi!")
