from random import randint, shuffle

doors = [True, False, False]
shuffle(doors)
guess_door = randint(0, 2)
revealed_door = randint(0, 2)
while revealed_door == guess_door or doors[revealed_door]:
    revealed_door = randint(0, 2)


