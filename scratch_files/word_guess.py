word = "PYTHONISTHEBEST"

scrambled = ["_" for _ in word]
print("".join(scrambled))

while "".join(scrambled) != word:
    print("Guess a letter.")
    guess = input().upper()
    if guess in word:
        # insane one-liner
        scrambled = [guess if word[i] == guess else scrambled[i] for i, n in enumerate(word) ]
    else:
        print("Not in word")
    print("".join(scrambled))
