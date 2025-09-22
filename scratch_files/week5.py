print("Are you using Celcius or Fahrenheit (C/F)?")
scale = input().upper()

while scale not in ["C", "F"]:
    print("Please submit either 'C' (Celcius) or 'F' (Fahrenheit).")
    scale = input().upper()

print("How many degrees?")
degrees = int(input())

if scale == "C":
    print(f"The result in Fahrenheit is {(degrees * (9 / 5)) + 32:.2f}")
else:
    print(f"The result in Celcius is {(degrees - 32) * (5 / 9):.2f}")
