# Using a list comprehension to generate
# the even numbers from 2 to 20

# a few ways to do this:
evens = [n for n in range(2, 21, 2)]
evens = [2 * n for n in range(1, 11)]

print(evens)


evens = [n for n in range(1, 21) if n % 2 == 0]
print(evens)
