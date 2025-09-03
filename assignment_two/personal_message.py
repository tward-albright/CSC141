# There's a few different ways to do this one, actually

name = "Eric"

# Concatenation w/ +
print("Hello " + name + ", how are you today?")

# f-strings
print(f"Hello {name}, how are you today?")

# Joining the strings (completely unnecessary)
print(", ".join(["Hello", name, "how are you today?"]))
