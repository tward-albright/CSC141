# I've decided to organize these by their order in the "Try It Yourself" boxes
# (part one is box one, etc.)
# 6-1
person = {"first_name": "Joe", "last_name": "Matto", "age": 200, "city": "Reading"}

for key, value in person.items():
    print(f"{key}: {value}")

print()  # for spacing

# 6-2, 6-10 and 6-12
favorite_numbers = {
    "Jovanny": [14, 34],
    "Marco": [67, 95],
    "Ethan": [12, 13, 14, 15],
    "Mario": [1, 3],
    "Chip": [25, 49, 30],
}

for name, numbers in favorite_numbers.items():
    formatted_numbers = ", ".join([str(n) for n in numbers])
    print(f"{name}'s favorite numbers are: {formatted_numbers}")

print()

# 6-3 and 6-4
glossary = {
    "Boolean": "A value that represents either true or false.",
    "Binary": "A base 2 counting system used often in computing.",
    "List": "An ordered representation of related items.",
    "Tuple": "An immutable ordered representation of related items.",
    "Set": "An unordered representation of unique items.",
}

for word, definition in glossary.items():
    print(f"{word}:\n  {definition}")
