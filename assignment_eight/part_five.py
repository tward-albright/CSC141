# 8-12
def make_sandwich(*toppings):
    print("Making a sandwich with: ")
    for topping in toppings:
        print(f"- {topping}")


make_sandwich("ham")
make_sandwich("ham", "american")
make_sandwich("ham", "american", "doritos")


# 8-13
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info["first_name"] = first
    user_info["last_name"] = last
    return user_info


user_profile = build_profile(
    "taylan", "ward", location="albright", field="compsci", favorite_color="lavendar"
)

print(user_profile)


# 8-14
def make_car(make, model, **qualities):
    qualities["make"] = make
    qualities["model"] = model
    return qualities


car = make_car("nissan", "altima", color="grey", subwoofer=False)
