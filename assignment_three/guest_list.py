guests = ["Harvey Milk", "Martin Luther King, Jr.", "David Lynch"]

for name in guests:
    print(f"Hello, {name}, would you like to join me for dinner?")


# 3-5
print("Sorry, Martin can't make it!")

guests[1] = "Ada Lovelace"

for name in guests:
    print(f"Hello, {name}, would you like to join me for dinner?")

# 3-6
print("There's a bigger table now!")

guests.insert(0, "Lady Gaga")
guests.insert(1, "Kendrick Lamar")
guests.append("Grant O'Brien")

# 3-10
print(f"We now have {len(guests)} people coming!")

# 3-7
print("Sorry; I can only invite two now!")

for i in range(4):
    kicked_out = guests.pop()
    print(f"Sorry, {kicked_out}, you have to go.")

for name in guests:
    print(f"Hey, {name}, you're still invited!")

del guests[0]
del guests[0]

print(guests)
