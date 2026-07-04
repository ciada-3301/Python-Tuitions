import random

# Fix 1: Correct the upper/lower bounds
lower = 100
upper = 500
seed = random.randint(lower, upper)

if seed % 2 != 0:
    seed += 1

# Generate the list (assume we don't know its length)
seedlings = [""] * seed
print(f"Secret total length created by system: {len(seedlings)}")

# Fix 2 & 3: Gross Division without using len() or list slicing
slow_index = 0
fast_index = 0

# We use an iterator to mimic streaming items without knowing the end
iterator = iter(seedlings)
divided = False

print("\nScanning list progressively...")
while not divided:
    try:
        # Move fast pointer 2 steps forward
        next(iterator)
        next(iterator)
        
        # Move slow pointer 1 step forward
        slow_index += 1
        fast_index += 2
        
    except StopIteration:
        # The fast pointer hit the end of the list!
        # The slow pointer is now perfectly at the midpoint.
        divided = True

# Validation
up_partition = seedlings[:slow_index]
low_partition = seedlings[slow_index:]

print("\nSolved!")
print(f"-> Calculated Midpoint Index: {slow_index}")
print(f"-> Upper segment count: {len(up_partition)}")
print(f"-> Lower segment count: {len(low_partition)}")
print(f"-> Balanced? {len(up_partition) == len(low_partition)}")
