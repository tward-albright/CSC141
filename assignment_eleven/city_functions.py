def make_city(city, country, population=0):
    if population > 0:
        return f"{city}, {country} - population {population}"
    return f"{city}, {country}"
