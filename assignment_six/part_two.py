# 6-5
rivers = {
    "Nile": "Egypt",
    "Mississippi": "Mississippi",
    "Mekong": "Laos",
    "Tiber": "Rome",
    "Ogun": "Nigeria",
}

for river, location in rivers.items():
    print(f"The {river} runs through {location}")

print()

# 6-6
need_to_poll = ["jen", "derrick", "phil", "tyler", "john"]
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "rust",
    "phil": "python",
}

for person in need_to_poll:
    if person in favorite_languages.keys():
        print(f"Thanks for taking the poll, {person}!")
    else:
        print(f"Hey, you should take that poll, {person}!")
