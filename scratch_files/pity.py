# Simulating the pity mechanics in gacha games
# pyright: strict, reportUnknownMemberType=false
from random import random
from matplotlib import pyplot as plt
import time

HARD_PITY = 90
SOFT_PITY = HARD_PITY - 10
PITY_BONUS = 0.01

ODDS = {"three_star": 0.5, "four_star": 0.4, "five_star": 0.085, "six_star": 0.015}


def sim():
    pull_count = 0
    past_pull_count = 0
    failed_pity = False
    while True:
        pull_count += 1
        pity_bonus = 0
        if pull_count >= SOFT_PITY:
            pity_bonus = PITY_BONUS * (HARD_PITY - pull_count)  # simplified, probably
        roll = random() - pity_bonus
        # print(roll)
        if roll <= ODDS["six_star"] or pull_count == HARD_PITY:
            roll = random()
            if roll >= 0.5 or failed_pity:
                # print("You got what you want!")
                break
            else:
                # print("You got what you didn't want!")
                failed_pity = True
                past_pull_count += pull_count
                pull_count = 0
    return pull_count + past_pull_count


start = time.time()
trials = [sim() for _ in range(1000000)]
end = time.time()
print(f"runtime: {end - start}s")
fig, ax = plt.subplots()
_ = ax.set_xlabel("Rolls used to get character")
_ = ax.hist(trials, bins=75)
plt.show()
