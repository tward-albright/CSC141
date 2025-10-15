# 7-1
car = input("What type of car would you like to rent? ")
print(f"Let's see if we can get a {car}")

# 7-2
guests = int(input("How many people are in your party? "))
if guests > 8:
    print("You'll have to wait for a table.")
else:
    print("Your table is ready!")

# 7-3
number = int(input("Pick a number: "))
if number % 10 == 0:
    print("Your number is a multiple of ten!")
else:
    print("Your number isn't a multiple of ten.")
