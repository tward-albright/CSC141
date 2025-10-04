# 6-7
people = [
    {"first_name": "Joe", "last_name": "Matto", "age": 200, "city": "Reading"},
    {"first_name": "Anita", "last_name": "Ward", "age": 38, "city": "Hampton"},
    {"first_name": "Gus", "last_name": "Trenor", "age": 45, "city": "Bellomont"},
]

for person in people:
    for key, value in person.items():
        print(f"{key}: {value}")
    print()

# 6-8
pets = [
    {"type": "dog", "owner": "Phil"},
    {"type": "bird", "owner": "Daryll"},
    {"type": "cat", "owner": "Shantae"},
]
for pet in pets:
    print(f"{pet['owner']} has a {pet['type']}!")
print()

# 6-9
favorite_places = {
    "Joe": ["New York", "Boston", "Chicago"],
    "Alex": ["Rome", "Stockholm", "London"],
    "Frank": ["Nuremburg", "Tokyo", "Cape Town"],
}

for person in favorite_places.keys():
    print(f"{person} likes {', '.join(favorite_places[person])}")
print()


# 6-11
cities = {
    "Boston": {
        "country": "USA",
        "population": "675,647",
        "fact": "Boston was the first city in the US with a subway.",
    },
    "Tokyo": {
        "country": "Japan",
        "population": "> 14,000,000",
        "fact": "Tokyo is the capital of Japan.",
    },
    "Cape Town": {
        "country": "South Africa",
        "population": "5,064,000",
        "fact": "Cape Town has been named the best city in the world.",
    },
}

for city in cities.keys():
    print(f"{city}")
    for k, v in cities[city].items():
        print(f"  {k}: {v}")
