# 7-8 and 7-9
sandwich_orders: list[str] = [
    "tuna",
    "pastrami",
    "pastrami",
    "chicken salad",
    "pastrami",
    "roast beef",
    "ham",
]
finished_sandwiches: list[str] = []

print("There's no pastrami at the deli!")
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

while sandwich_orders:
    current = sandwich_orders.pop()
    print(f"Making a {current} sandwich...")
    finished_sandwiches.append(current)

print("Finished sanwiches: ")

for sandwich in finished_sandwiches:
    print(f"{sandwich} sandwich")

# 7-10
responses: list[str] = []
while True:
    print("What's your dream vacation (q to quit)?")
    reply = input()

    if reply.lower() == "q":
        break

    responses.append(reply)

for response in responses:
    print(f"- {response}")
