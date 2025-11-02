from random import randint, choice


# 9-13
class Die:
    def __init__(self, sides):
        self.sides = sides

    def roll(self):
        print(f"Rolling d{self.sides}: {randint(1, self.sides)}")


d6 = Die(6)
d10 = Die(10)
d20 = Die(20)

for _ in range(10):
    d6.roll()
    d10.roll()
    d20.roll()

# 9-14 and 9-15
lottery_values = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "A", "B", "C", "D", "E")
winning_ticket = []
for _ in range(4):
    winning_ticket.append(choice(lottery_values))
print(f"Any ticket matching {winning_ticket} wins!")

tries = 0
my_ticket = []
while my_ticket != winning_ticket:
    tries += 1
    my_ticket = []
    for _ in range(4):
        my_ticket.append(choice(lottery_values))

print(f"Took {tries} attempts to win!")
