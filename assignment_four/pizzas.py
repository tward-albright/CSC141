pizzas = ["white pizza", "cheese pizza", "pepperoni pizza"]

for pizza in pizzas:
    print(f"I love {pizza}!")

print("I like pizza!")

# 4-11

friends_pizzas = pizzas[:]
pizzas.append("meatball pizza")
friends_pizzas.append("ultimate pizza")

print("My favorite pizzas are: ")
for pizza in pizzas:
    print(pizza)

print("My friend's favorite pizzas are: ")
for pizza in friends_pizzas:
    print(pizza)
