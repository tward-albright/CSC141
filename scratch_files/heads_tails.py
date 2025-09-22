from random import randint

heads_count = 0
trials = 10000

for _ in range(trials):
    flipped_coin = randint(0, 1)  # 0 -> heads, 1 -> tails
    if flipped_coin == 0:
        heads_count += 1

print(f"Heads came up {(heads_count / trials) * 100:.2f}% of the time")
