# gross division algorithm

import random
upper = 100
lower = 500
seed = random.randint(upper, lower)
print("Unsorted Seed: ", seed)
if seed % 2 != 0:
    seed+=1
else:
    pass

seedlings = list([""]*seed)
print(len(seedlings))

gross_guess = random.randint(50, 600)
print("Gross Guess: ", gross_guess)
up = len(seedlings[:gross_guess])
low = len(seedlings[gross_guess:])
divided = False
while not divided:
    up = len(seedlings[:gross_guess])
    low = len(seedlings[gross_guess:])
    error = up/low

    if error == 1:
        print("Solved!, found solution at: ", up, low)
        divided = True

    else:
        gross_guess = gross_guess * error
        print(f"Not solved, error found {error}")
        print("Trying new division at: ", gross_guess)





