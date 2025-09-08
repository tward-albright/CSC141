visited_cities = ["Kyoto", "Tokyo", "Tokyo", "Shibuya", "Osaka"]

print("In Japan, I've visited:")

print(visited_cities)

print("I've also visited Nara, so I'll add it.")

visited_cities.append("Nara")
print(visited_cities)

print("I shopped in Harajuku, so I'll add that too")

visited_cities.insert(2, "Harajuku Shopping District")
print(visited_cities)

invalid = visited_cities.pop(2)
print(f"Technically, the {invalid} is not an city.")
print(visited_cities)

print("Whoops, I put Tokyo twice!")
visited_cities.remove("Tokyo")
print(visited_cities)

print("Let's sort these.")
visited_cities.sort()
print(visited_cities)
