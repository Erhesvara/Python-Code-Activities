import random


def coin_flip():
    """Randomly return 'heads' or 'tails'."""
    if random.randint(0, 1) == 0:
        return "heads"
    else:
        return "tails"


heads_tally = 0
tail_tally = 0

for trial in range(10_000):
    if coin_flip() == "heads":
        heads_tally = heads_tally + 1
    else:
        tail_tally = tail_tally + 1

print(f"for the tail tally {tail_tally}")
print(f"for the head tally {heads_tally}")


# Unfair coin toss
def unfair_coin_flip(probability_of_tails):
    if random.random() < probability_of_tails:
        return "tails"
    else:
        return "heads"


heads_tally1 = 0
tail_tally1 = 0

for trial in range(10_000):
    if unfair_coin_flip(.7) == "heads":
        heads_tally1 = heads_tally1 + 1
    else:
        tail_tally1 = tail_tally1 + 1

print(f"for the tail tally {tail_tally1}")
print(f"for the head tally {heads_tally1}")
