# 4-3
for i in range(1, 21):
    print(i)

# 4-4
one_mil = range(1, 1000001)
for n in one_mil:
    # print(n) # removed to test the rest of the program
    pass

# 4-5
print(min(one_mil))
print(max(one_mil))

print(sum(one_mil))

# 4-6
for i in range(1, 21, 2):
    print(i)

# 4-7
threes = range(3, 31, 3)
for three in threes:
    print(three)

# 4-8
for i in range(1, 11):
    print(i**3)

# 4-9
cubes = [i**3 for i in range(1, 11)]
