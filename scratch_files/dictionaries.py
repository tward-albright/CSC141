from random import choice

employees = {
    "Brian": {"salary": 25, "age": 40},
    "Sarah": {"salary": 25, "age": 40},
    "Peter": {"salary": 25, "age": 40},
    "Mary": {"salary": 25, "age": 40}
}


keypad = {
    "1": ["1"],
    "2": ["A", "B", "C"],
    "3": ["D", "E", "F"],
    "4": ["G", "H", "I"],
    "5": ["J", "K", "L"],
    "6": ["M", "N", "O"],
    "7": ["P", "Q", "R", "S"],
    "8": ["T", "U", "V"],
    "9": ["W", "X", "Y", "Z"],
    "0": ["0"]
}

phone_number = "8775309"
# vanity_number = "877CASHNOW"
mnemonic = ""
for digit in phone_number:
    mnemonic += choice(keypad[digit])
print(mnemonic)
