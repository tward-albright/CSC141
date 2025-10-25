# 8-6
def city_country(city, country):
    return f"{city}, {country}"


print(city_country("Sydney", "Australia"))
print(city_country("Seattle", "USA"))
print(city_country("Cape Town", "South Africa"))


# 8-7 & 8-8
def make_album(artist, title, length=None):
    album = {
        "artist": artist,
        "title": title,
    }
    if length:
        album["length"] = length

    return album


print(make_album("Deftones", "White Pony"))
print(make_album("Moore Kismet", "Saturate Your World"))
print(make_album("Kendrick Lamar", "gnx"))
