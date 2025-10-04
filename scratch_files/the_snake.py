# Taylan Ward; CSC141
#
# Remaking a Matt Parker video simulation where he sees
# the probability of rolling snake eyes (two ones) on dice
# and graphing it.

from random import random
import matplotlib.pyplot as plt
#import numpy as np

def simulate_roll():

    if random() <= (1/36):
        return True

    return False

def trials(count: int) -> list[int]:
    roll_counter: list[int] = []
    for i in range(count):
        rolls_used = 0
        snake_eyes = 0
        while True:
            rolls_used += 1
            if simulate_roll():
                snake_eyes += 1
            if snake_eyes == 5:
                break
        roll_counter.append(rolls_used)
    return roll_counter

fig, ax = plt.subplots()
ran_trials = trials(1000000)
ax.set_xlabel("Number of rolls")
ax.hist(ran_trials, bins=1000)
_ = plt.show()
